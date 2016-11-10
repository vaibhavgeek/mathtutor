from flask import Flask, request
import requests
import json
import traceback
import random
from constants import *
import os
from util import *
from pymongo import MongoClient
from flask import render_template


app = Flask(__name__)

client = MongoClient(CONNECTION)
db = client.mathman


@app.route('/webhook', methods=['GET'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge', '')
        else:
            return render_template("privacy.html")


@app.route('/webhook', methods=['POST'])
def handle_message():
    try:
        data = request.json 
        if get_message(data):
            message_t , sed_id = get_message(data)
            if "solve" in message_t.lower(): 
                showResults(sed_id , message_t)
            print message_t
    except:
        pass            
    try:
        user = None
        payload = request.get_data()
        sender, message = messaging_events(payload)
        user = db.user.find_one({"fbId": sender})
        if user is None:
            db.user.insert(
                {"fbId": sender, "level": "Expert", "isFirstTime": True, "correctQuestions" : 3})
            user = db.user.find_one({"fbId": sender})

        if message == "Start":
            send_button_template_message(
                sender,
                "Great, What do you want to do ?",
                [
                    generate_button("Learn & Practice", "LEARN"),
                    generate_button("Ask Doubts", "USER_DEFINED_PAYLOAD")
                ]
            )
        elif message == "LEARN":
            send_carasol_items(
                sender,
                [
                    generate_carasol_items(
                        "Operation on numbers",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Arithmetic_symbols.svg/2000px-Arithmetic_symbols.svg.png",
                        "ON"),
                    generate_carasol_items(
                        "Linear Equations in two varaibles",
                        "http://www.mycompasstest.com/wp-content/uploads/2011/01/BBlintwo.png",
                        "LINEAR"),
                    generate_carasol_items(
                        "Quadratic Equations",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/e3/Quadratic-equation.svg/769px-Quadratic-equation.svg.png",
                        "QUAD"),
                    generate_carasol_items(
                        "Basic Trignometry",
                        "https://www.mathsisfun.com/images/adjacent-opposite-hypotenuse.gif",
                        "BT")])

        elif message == "ON":
            if user["isFirstTime"]:
                db.user.update({"fbId": user["fbId"]}, {
                               "$set": {"isFirstTime": False}})
                send_text_message(
                    sender,
                    "Hey! Let's start with some questions so we can know how good you are with particular topic.")
                questionToAsk = medium_operation()
                send_text_message(sender, questionToAsk["question"])
                db.user.update({"fbId": user["fbId"]}, {
                               "$set": {"lastQuestion": questionToAsk["question"]}})
                buttons = [
                    generate_button("A " + str(questionToAsk["option1"]), payload='incorrect1'),
                    generate_button("B " + str(questionToAsk["option2"]), payload='incorrect2'),
                    generate_button("C " + str(questionToAsk["option3"]), payload='incorrect3')
                ]
                buttons[questionToAsk["answer"]]["payload"] = 'correct'
                send_button_template_message(
                    sender,
                    "Select Your Choice",
                    buttons
                )
            else:
                askQuestion(sender, message)

        elif message == "LINEAR":
            if user["isFirstTime"]:
                db.user.update({"fbId": user["fbId"]}, {
                               "$set": {"isFirstTime": False}})
                send_text_message(
                    sender,
                    "Hey! Let's start with some questions so we can know how good you are with particular topic.")
                questionToAsk = linear_hard()
                send_text_message(sender, questionToAsk["question"])
                db.user.update({"fbId": user["fbId"]}, {
                               "$set": {"lastQuestion": questionToAsk["question"]}})
                buttons = [
                    generate_button("A " + str(questionToAsk["option1"]), payload='incorrect1'),
                    generate_button("B " + str(questionToAsk["option2"]), payload='incorrect2'),
                    generate_button("C " + str(questionToAsk["option3"]), payload='incorrect3')
                ]
                buttons[questionToAsk["answer"]]["payload"] = 'correct'
                send_button_template_message(
                    sender,
                    "Select Your Choice",
                    buttons
                )
            else:
                askQuestion(sender, message)


        elif message == 'QUAD':
            if user["isFirstTime"]:
                db.user.update({"fbId": user["fbId"]}, {
                               "$set": {"isFirstTime": False}})
                send_text_message(
                    sender,
                    "Hey! Let's start with some questions so we can know how good you are with particular topic.")
                questionToAsk = quadhard()
                send_text_message(sender, questionToAsk["question"])
                db.user.update({"fbId": user["fbId"]}, {
                               "$set": {"lastQuestion": questionToAsk["question"]}})
                buttons = [
                    generate_button("A " + str(questionToAsk["option1"]), payload='incorrect1'),
                    generate_button("B " + str(questionToAsk["option2"]), payload='incorrect2'),
                    generate_button("C " + str(questionToAsk["option3"]), payload='incorrect3')
                ]
                buttons[questionToAsk["answer"]]["payload"] = 'correct'
                send_button_template_message(
                    sender,
                    "Select Your Choice",
                    buttons
                )
            else:
                askQuestion(sender, message)

        elif message == "correct":
            send_text_message(sender, "Congralutions you are correct :D")
            showResults(sender, user["lastQuestion"])
            db.user.update({"fbId" : sender}, {"$inc" : {'correctQuestions' : 1}})
            user = db.user.find_one({"fbId" : sender})
            if user["correctQuestions"] == 3:
                db.user.update({"fbId" : sender}, {"$set" : {'correctQuestions' : 0}})
                if user["level"] == "medium":
                    db.user.update({"fbId" : sender}, {"$set" : {'level' : "Expert"}})
                elif user["level"] == "noob":
                    db.user.update({"fbId" : sender}, {"$set" : {'level' : "medium"}})
            askQuestion(sender, message)

        elif message in "incorrect":
            send_text_message(sender, "Oops sounds like you made a mistake :(")
            send_image(sender, "Here is a video tutorial which can help you to learn better")
            showResults(sender, user["lastQuestion"])
            db.user.update({"fbId" : sender}, {"$set" : {'correctQuestions' : 0}})
            user = db.user.find_one({"fbId" : sender})
            if user["correctQuestions"] == 0 or user["correctQuestions"] == -3:
                if user["level"] == "Expert":
                    db.user.update({"fbId" : sender}, {"$set" : {'level' : "medium"}})
                elif user["level"] == "medium":
                    db.user.update({"fbId" : sender}, {"$set" : {'level' : "noob"}})
            askQuestion(sender, message)
        elif message == 'USER_DEFINED_PAYLOAD':
            send_text_message(sender, "Simply send the question in text, our advance AI engine will try to understand it. Type 'Solve' followed by the question")    
            
        return "ok" 
    except:
        print "message with shit"
        return "Hello World"


def askQuestion(recipent, chapter):
    user = db.user.find_one({"fbId" : recipent})
    questionToAsk = linear_hard()
    if user["level"] == 'Expert':
        if chapter == 'ON':
            questionToAsk = advacned_operation()
        elif chapter == 'Linear':
            questionToAsk = linear_hard()
        elif chapter == 'QUAD':
            questionToAsk = quadhard()

    elif user["level"] == "medium":
        if chapter == 'ON':
            questionToAsk = medium_operation()
        elif chapter == 'Linear':
            questionToAsk = linear_medium()
        elif chapter == 'QUAD':
            questionToAsk = quadmedium()

    elif user["level"] == "noob":
        if chapter == 'ON':
            questionToAsk = easy_multiply()
        elif chapter == 'Linear':
            questionToAsk = linear_easy()
        elif chapter == 'QUAD':
            questionToAsk = quadeasy()


    send_text_message(recipent, questionToAsk["question"])
    db.user.update({"fbId": user["fbId"]}, {
                   "$set": {"lastQuestion": questionToAsk["question"]}})
    buttons = [
        generate_button("A " + str(questionToAsk["option1"]), payload='incorrect'),
        generate_button("B " + str(questionToAsk["option2"]), payload='incorrect'),
        generate_button("C " + str(questionToAsk["option3"]), payload='incorrect')
    ]
    buttons[questionToAsk["answer"]]["payload"] = 'correct'
    send_button_template_message(
        recipent,
        "Select Your Choice",
        buttons
    )


def showResults(sender, question):
    try:
        data = get_solution_from_wolfarmAlpha(question)
        items = []
        for item in data:
            send_image(sender, item["img"])
    except:
        pass

def init():
    r = requests.post(THREAD_URL,
                      params={"access_token": PAT},
                      data=json.dumps({
                          "setting_type": "call_to_actions",
                          "thread_state": "new_thread",
                          "call_to_actions": [
                              {
                                  "type": "postback",
                                  "title": "Start",
                                  "payload": "Start"
                              }
                          ]
                      }),
                      headers={'Content-type': 'application/json'}
                      )
    print r.text

    r = requests.post(THREAD_URL,
                      params={"access_token": PAT},
                      data=json.dumps({
                          "setting_type": "call_to_actions",
                          "thread_state": "existing_thread",
                          "call_to_actions": [
                              {
                                  "type": "postback",
                                  "title": "Learn & Practice",
                                  "payload": "LEARN"
                              },
                              {
                                  "type": "postback",
                                  "title": "Ask Doubts",
                                  "payload": "USER_DEFINED_PAYLOAD"
                              }
                          ]
                      }),
                      headers={'Content-type': 'application/json'}
                      )
    print r.text




if __name__ == '__main__':
    init()
    port = int(os.environ.get('PORT', 33507))
    app.run(host="0.0.0.0", port=port, debug=True)
