from flask import Flask
from flask import request
import json
import requests
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from datetime import timedelta, timezone, datetime

app = Flask(__name__, static_folder='../client/build', static_url_path='/')
app.config["JWT_SECRET_KEY"] = "25e717c1bc3549b454d91379f82380bb509bf953f345e45c0b08849c50004ac1"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route("/api/auth")
def auth():
    code = request.args.get('code')
    try:
        client_secret = '1b3911f47e062fb0ab2427428de713ef'
        files = {
            'client_id': (None, '283690477978497'),
            'client_secret': (None, client_secret),
            'grant_type': (None, 'authorization_code'),
            'redirect_uri': (None, 'https://amyjbaer.pythonanywhere.com/auth'),
            'code': (None, code),
        }

        response = requests.post('https://api.instagram.com/oauth/access_token', files=files)
        data = response.json()
        insta_token = data.get("access_token")
        if not insta_token:
            raise Exception("access token not found " + response.text)
        access_token = create_access_token(identity=data["access_token"])
        # short_term_resp = {"access_token": "IGQWRPUzl4NE9INm8zT3B6YnRmMTBIUXE2c0dKNEdNVFpOcHVGNVdCcG1kdFlObVFrUFd3NVl1NjBYRUJ1ZA1FUTVJHdzJxTlpQMDFYbW1xblUzRW1lYzZAiZAW5BcTA0TS11aThrTWVNekJmUmlrcy1yV1VlUUx2ay1ZAUTYzSk5ZAWWxpQQZDZD", "user_id": 6787951627954458}
        
        # response = requests.get(
        #     f'https://graph.instagram.com/access_token?grant_type=ig_exchange_token&client_secret={client_secret}&access_token={short_term_resp["access_token"]}'
        # )
        return {"access_token": access_token}
    except Exception as e:
        return {"error": str(e)}

@app.route('/api/user')
@jwt_required
def user():
    try:
        token = get_jwt_identity()
        response = requests.get(f'https://graph.instagram.com/me?fields=id,username&access_token={token}')
        return response
    except Exception as e:
        return json.dumps(e)

# @app.after_request
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.now(timezone.utc)
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
#         if target_timestamp > exp_timestamp:
#             access_token = create_access_token(identity=get_jwt_identity())
#             data = response.get_json()
#             if type(data) is dict:
#                 data["access_token"] = access_token 
#                 response.data = json.dumps(data)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original respone
#         return response


@app.route("/logout")
def logout():
    response = json.dumps({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

if __name__ == "__main__":
    app.run(debug=True)