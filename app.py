from flask import Flask, request
import requests
import json
import traceback
import random
from constants import *
import os
from util import *

app = Flask(__name__)



@app.route('/webhook', methods = ['GET'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge','')
        else:
            return "It's working well"

@app.route('/webhook', methods = ['POST'])
def handle_message():
    try:
        payload = request.get_data()
        sender, message = messaging_events(payload)
        if message == "click":
            send_typing_status(sender)
            send_button_template_message(sender, "Choose from the below",[
                generate_button("Hello", "HelloButton"),
                generate_button("How are you ?", "HelloButton")
            ])
        else:
            send_text_message(sender, message)
        return "ok"
    except:
        print "message with shit"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host = "0.0.0.0",port = port, debug = True)
