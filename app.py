from flask import Flask, request
import requests
import json
import traceback
import random
from constants import *
import os
from util import send_text_message
from util import messaging_events

app = Flask(__name__)

PAT = 'EAANHAD7qAxkBAH4ZAZBdmXZAqAC3kYK5YjKngMo1HPVKMIp95dLl6fwBwvptwHg9WQFNWBYcVkaW1k8AiFAZA4vM0rzwlTBdIp5y4R95aZByoemeBPJDrOKXryq0RLNlzZBv6ZCMwuZB9YXsP2w2ghuZB70PDsPg7oYGbYOZB3sAdwDAZDZD'

@app.route('/webhook', methods = ['GET'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge','')
        else:
            return "It's working well"

@app.route('/webhook', methods = ['POST'])
def handle_message():
    print "Handling Messages"
    payload = request.get_data()
    print payload
    for sender, message in messaging_events(payload):
        print "Incoming from %s: %s" % (sender, message)
        send_message(PAT, sender, message)
    return "ok"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host = "0.0.0.0",port = port)
