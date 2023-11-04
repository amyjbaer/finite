from flask import Flask
import time
from flask import request
import json
import requests

app = Flask(__name__)

@app.route("/api/auth")
def auth():
    code = request.args.get('code')
    try: 
        files = {
            'client_id': (None, '283690477978497'),
            'client_secret': (None, '1b3911f47e062fb0ab2427428de713ef'),
            'grant_type': (None, 'authorization_code'),
            'redirect_uri': (None, 'https://willowy-biscuit-0a7ec9.netlify.app/api/auth'),
            'code': (None, code),
        }

        response = requests.post('https://api.instagram.com/oauth/access_token', files=files)
        return response.text
    except Exception as e:
        return json.dumps(e)

if __name__ == "__main__":
    app.run(debug=True)