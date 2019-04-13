# Skeleton-Slackbot
This is starter code for making a python slackbot that uses [python's slackclient] package based on the slack [RTM API]. 
## Setup
Before anything else, you should have python (version 3 or later) installed along with pip, a python package manager. You will need to run the following command in order to run the bot:
```
$ pip install slackclient
```
## Usage
First you need to [create a new slack app]. Then add it to the slack space you wish to use it in (for the case of this workshop, please add it to slackbothaven). **Make sure to add a bot user before trying to install the app to your workspace.**  
Get the Bot User OAuth Access Token after installign it and run the following command in your cloned directory:
```
$ SLACK_BOT_TOKEN="xoxb-xxxxxxxxxxx-yyyyyyyyyyy-zzzzzzzzzzz" python ./slack-bot.py
```
Test that your bot is working by @ing it.

[python's slackclient]: https://github.com/slackapi/python-slackclient
[RTM API]: <https://api.slack.com/rtm>
[create a new slack app]: <https://api.slack.com/apps>
