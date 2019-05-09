import os
import time
from slackclient import SlackClient
from random import randint

answers = [
    "Maybe.",
    "I don't think so.",
    "Yes.",
    "Try asking again.",
    "No.",
    "Definitely.",
    ":thumbsup:",
    ":thumbsdown:",
    ":100:",
    ":ok_hand:",
    "No doubt.",
    "That's gonna be a no from me.",
    "Fuck no.",
    "Hell yeah.",
    ":grimacing:",
    ":scream:",
    ":slightly_smiling_face:",
    ":grinning:",
    "Of course."
]

def bestowWisdom(slackClient, user, text_received, channel, ts):
    text_received = text_received.split()

    if len(text_received) > 1:
      slackClient.api_call(
        "chat.postMessage",
        channel = channel,
        thread_ts = ts,
        text = "<@{user}> {answer}".format(user=user, answer=answers[randint(0, len(answers) - 1)]
      ))

def parse_bot_commands(events):
    for event in events:
        if event['type'] == 'message' and not "subtype" in event:
            user_id = event["user"]
            text_received = event["text"]
            channel = event["channel"]
            ts = event["ts"]
            if '@%s' %bot_id in text_received:
                bestowWisdom(client, user_id, text_received, channel, ts)

token= os.environ["SLACK_API_TOKEN"]
client= SlackClient(token)

if client.rtm_connect(auto_reconnect=True):
    bot_id=client.api_call("auth.test")["user_id"]
    while True:
        parse_bot_commands(client.rtm_read())
        time.sleep(1)
