import requests
import os
import json
import webbrowser
from flask import Flask, request

app = Flask(__name__)
global_access_token = None

client_id = os.environ.get('STRAVA_CLIENT_ID')
client_secret = os.environ.get('STRAVA_CLIENT_SECRET')
auth_url = f"https://www.strava.com/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri=http://127.0.0.1:5000/exchange_token&approval_prompt=force&scope=read,activity:read_all"
token_url = "https://www.strava.com/oauth/token"

webbrowser.open(auth_url, new=1)

@app.route('/exchange_token')
def exchange_token():
    global global_access_token
    code = request.args.get('code')
    
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'grant_type': 'authorization_code'
    }

    response = requests.post(token_url, params=params)
    token_data = json.loads(response.text)
    global_access_token = token_data['access_token']
    
    return "Authorized successfully. You can close this window."

@app.route('/download_activities')
def download_activities():
    if global_access_token:  # Make sure the token is available
        activities = get_activities(global_access_token)
        
        # Save to a JSON file
        with open("activities.json", "w") as f:
            json.dump(activities, f)
        
        return "Activities downloaded and saved."
    else:
        return "No access token available."

def get_activities(access_token):
    url = "https://www.strava.com/api/v3/activities"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)








