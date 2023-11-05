from flask import Flask
from flask import request
import json
import requests
import git

app = Flask(__name__, static_folder='../client/build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/api/auth")
def auth():
    code = request.args.get('code')
    try: 
        files = {
            'client_id': (None, '283690477978497'),
            'client_secret': (None, '1b3911f47e062fb0ab2427428de713ef'),
            'grant_type': (None, 'authorization_code'),
            'redirect_uri': (None, 'https://amyjbaer.pythonanywhere.com/api/auth'),
            'code': (None, code),
        }

        response = requests.post('https://api.instagram.com/oauth/access_token', files=files)
        return response.text
    except Exception as e:
        return json.dumps(e)

@app.route('/api/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('..')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

if __name__ == "__main__":
    app.run(debug=True)