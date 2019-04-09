import os
import time
from slackclient import SlackClient

def sayHi(slackClient, user):
    slackClient.api_call(
    "chat.postMessage",
    channel='slack-bots',
    text='yo, <@%s>' %user)

def parse_bot_commands(events):
    for event in events:
        if event['type']== 'message' and not "subtype" in event:
            user_id, text_received, channel=event['user'], event['text'], event['channel']
            if '@%s' %bot_id in text_received:
                sayHi(client, user_id)

token= os.environ["SLACK_API_TOKEN"]
client= SlackClient(token)
if client.rtm_connect(auto_reconnect=True):
    bot_id=client.api_call("auth.test")["user_id"]
    while True:
        #print (client.rtm_read())
        parse_bot_commands(client.rtm_read())
        time.sleep(1)
