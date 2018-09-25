import requests
import json
import os

payload = {
    'part' : 'snippet',
    'channelId' : os.environ['C_ID'],
    'type' : 'video',
    'eventType' : 'live',
    'key' : os.environ['YLN_KEY']
}

r = requests.get('https://www.googleapis.com/youtube/v3/search', params = payload).json()

try:
    info = r["items"][0]["snippet"]["liveBroadcastContent"]
except:
    ## no live
    print("error")
else:
    ## live now
    if info == "live":
        send_text = 'Start live at "' + r["items"][0]["snippet"]["channelTitle"] + '" : "' + r["items"][0]["snippet"]["title"] + '"'
        payload_post ={
            'text' : send_text
        }
        url = 'https://hooks.slack.com/services/' + os.environ['SLACK_URL']
        requests.post(url, data = json.dumps(payload_post))
