import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
client = WebClient(token='xoxb-1374815456550-1595112250132-ICKNalrFJ5R3mksGnaQinN2Z')
try:
    response = client.chat_postMessage(channel='#bot-channel', text="Welcome to SDA Slack Bot!")
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")