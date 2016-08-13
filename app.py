from flask import Flask, request
import requests
import json
import traceback
import random
from constants import *
import os
from util import *
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(CONNECTION)
db = client.mathman

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
        user = None
        payload = request.get_data()
        sender, message = messaging_events(payload)
        user = db.user.find_one({"fbId" : sender})
        if user is None:
            db.user.insert({"fbId" : sender, "level" : "expert", "isFirstTime" : True})
            user = db.user.find_one({"fbId" : sender})

        if message == "Start":
            send_button_template_message(
            sender,
            "Great, What do you want to do ?",
            [
                generate_button("Learn & Practice", "LEARN"),
                generate_button("Ask Doubts", "ASK"),
                generate_button("Solve Math Puzzles", "PUZZ")
            ]
        )
        elif message == "LEARN":
            send_carasol_items(
                sender,
                [
                    generate_carasol_items("Operation on numbers", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Arithmetic_symbols.svg/2000px-Arithmetic_symbols.svg.png", "ON"),
                    generate_carasol_items("Linear Equations in two varaibles", "http://www.mycompasstest.com/wp-content/uploads/2011/01/BBlintwo.png", "LINEAR"),
                    generate_carasol_items("Quadratic Equations", "https://upload.wikimedia.org/wikipedia/en/thumb/e/e3/Quadratic-equation.svg/769px-Quadratic-equation.svg.png", "QUAD"),
                    generate_carasol_items("Basic Trignometry", "https://www.mathsisfun.com/images/adjacent-opposite-hypotenuse.gif", "BT")
                ]
            )

        elif message == "ON":
            if user["isFirstTime"]:
                db.user.update({"fbId" : user["fbId"]}, {"$set" : {"isFirstTime" : False}})
                send_text_message(sender, "Hey! Let's start with some questions so we can know how good you are with particular topic.")
                

        return "ok"
    except:
        print "message with shit"

def init():
    r = requests.post(THREAD_URL,
          params = {"access_token" : PAT},
          data = json.dumps({
                "setting_type" : "call_to_actions",
                "thread_state" : "new_thread",
                "call_to_actions" : [
                    {
                        "type" : "postback",
                        "title" : "Start",
                        "payload" : "Start"
                    }
                ]
          }),
          headers = {'Content-type' : 'application/json'}
    )
    print r.text

    r = requests.post(THREAD_URL,
          params = {"access_token" : PAT},
          data = json.dumps({
                "setting_type" : "call_to_actions",
                "thread_state" : "existing_thread",
                "call_to_actions" : [
                    {
                        "type" : "postback",
                        "title" : "Learn & Practice",
                        "payload" : "LEARN"
                    },
                    {
                        "type" : "postback",
                        "title" : "Ask Doubts",
                        "payload" : "ASK"
                    }
                ]
          }),
          headers = {'Content-type' : 'application/json'}
    )
    print r.text


if __name__ == '__main__':
    init()
    port = int(os.environ.get('PORT', 33507))
    app.run(host = "0.0.0.0",port = port, debug = True)
