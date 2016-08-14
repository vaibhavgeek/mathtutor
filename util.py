import json
import requests
from constants import SEND_MESSAGE_URL, PAT as token
from random import randint
import random
import xml.etree.ElementTree
import math


def send_typing_status(recipient):
  """Send the message text to recipient with id recipient.
  """
  r = requests.post(SEND_MESSAGE_URL,
    params={"access_token": token},
      data=json.dumps({
          "recipient": {"id": recipient},
      "sender_action": "typing_on"
    }),
      headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text

def get_solution_from_wolfarmAlpha(question):
    url = "http://api.wolframalpha.com/v2/query"
    params = {"input" : question, "appid" : "Q7K5HX-2Y24EKLAQW", "format" : 'image,plaintext'}
    r = requests.get(url, params = params)
    root = xml.etree.ElementTree.fromstring(r.text)
    response = []
    count = 0
    for f in root:
        if count == 0:
            count = count + 1
            continue
        temp = {}
        temp["title"] = f.attrib['title']
        temp["img"] = f[0][0].attrib['src']
        response.append(temp)
    return response

def send_text_message(recipient, text):
  """Send the message text to recipient with id recipient.
  """

  r = requests.post(SEND_MESSAGE_URL,
    params={"access_token": token},
      data=json.dumps({
          "recipient": {"id": recipient},
      "message": {"text": text.decode('unicode_escape')},
    }),
      headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text


def send_button_template_message(recipient, text, buttons):
    r = requests.post(SEND_MESSAGE_URL,
          params={'access_token': token},
          data=json.dumps({
              "recipient": {"id": recipient},
              "message": {
                  "attachment": {
                  "type": "template",
                  "payload": {
                      "template_type": "button",
                      "text": text,
                      "buttons": buttons
                  }
              }}
          }),
          headers={'Content-type': 'application/json'})
    print r.text


def send_image(recipent, item, type="image"):
    r = requests.post(SEND_MESSAGE_URL, params = {'access_token' : token},
            data = json.dumps({
                "recipient" : {"id" : recipent},
                "message" : {
                    "attachment" : {
                        "type" : type,
                        "payload" : {
                            "url" : item
                        }
                    }
                }
            }),
            headers = {'Content-type' : 'application/json'}
        )
    print r.text

def send_carasol_items(recipient, items):
    r = requests.post(SEND_MESSAGE_URL,
          params={'access_token': token},
          data=json.dumps({
              "recipient": {"id": recipient},
              "message": {"attachment":
                    {
                        "type": "template",
                        "payload": {
                          "template_type": "generic",
                          "elements": items
                      }
                 }
            }
        }),
        headers={'Content-type': 'application/json'})
    print r.text


def generate_carasol_items(text, image_url, payload = None, showbtns = True):
    if showbtns:
        return {
            "title": text,
            "image_url": image_url,
            "buttons": [
                {
                    "type": "postback",
                    "title": "Learn This",
                    "payload": payload
                }
            ]
        }
    else:
        return {
            "title": text,
            "image_url": image_url,
        }



def generate_button(text, payload=None, type="text", url=None):
    if type == "url":
        return {
            "type": "web_url",
            "url": url,
            "title": text
        }
    else:
        return {
            "type": "postback",
            "title": text,
            "payload": payload
        }


def messaging_events(payload):
    """Generate tuples of (sender_id, message_text) from the
    provided payload.
    """
    data = json.loads(payload)
    messaging_events = data["entry"][0]["messaging"]
    for event in messaging_events:
        if "message" in event and "text" in event["message"]:
            return (event["sender"]["id"], event["message"]
                ["text"].encode('unicode_escape'))
        elif "postback" in event and "payload" in event["postback"]:
            return (event["sender"]["id"], event["postback"]["payload"])

def quadeasy():
    a = randint(1,7)
    c = randint(1,40)
    b = 2 * math.sqrt(a*c)
    while(math.sqrt(a*c).is_integer() == False):
        c = c+1
    b = int(2 * math.sqrt(a*c))
    answer = float(-1 * b )/(2*a)
    question = "Solve the Equation %sx^2 + %sx + %s = 0" %(a ,b ,c )
    option1 = answer - randint(1,3)
    option2 = answer + randint(3,5)
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand  }
    return dict

def quadmedium():
    a = randint(1,7)
    b = randint(15,30)
    c = randint(2,5)
    while(math.sqrt((b*b) - (4*a*c)).is_integer() == False):
        c = c+1
    answer = ((-b) + (math.sqrt((b*b) - (4*a*c))))/ (2 * a)
    question = "Solve the Equation %sx^2 + %sx + %s = 0" %(a ,b ,c )
    option1 = answer - randint(1,3)
    option2 = answer + randint(3,5)
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand }
    return dict

def quadhard():
    a = randint(4,7)
    b = randint(19,32)
    c = randint(3,10)
    while(math.sqrt((b*b) - (4*a*c)).is_integer() == False):
        c = c+1
    question = "Solve the Equation %sx^2 + %sx + %s = 0" %(a ,b ,c )
    answer = ((-b) + (math.sqrt((b*b) - (4*a*c))))/ (2 * a)
    option1 = answer - randint(1,3)
    option2 = answer + randint(3,5)
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand  }
    return dict

def linear_easy():
    a = randint(4,6)
    b = 1
    c = 0
    d = randint(1,4)
    e = randint(1,4)
    f = randint(5,10)
    question = 'Solve the linear equations %sx + %sy = 0 and %sx + %sy + %s = 0' %(a,b,d,e,f)
    answer_1 = b*f
    answer_2 = e*c
    answer_3 = e*a
    answer_4 = b*d
    answer_5 = d*c
    answer_6 = f*a
    final_answer_1 = float(answer_1 - answer_2) / (answer_3 - answer_4)
    final_answer_2 = float(answer_5 - answer_6) / (answer_3 - answer_4)
    answer = "(" + "{:.2f}".format(final_answer_1) + ", " + "{:.2f}".format(final_answer_2) + ")"
    option1 = "(" + ("{:.2f}".format(final_answer_1+ 0.23))  + ", " + ("{:.2f}".format(final_answer_2+0.23))  + ")"
    option2 = "(" + ("{:.2f}".format(final_answer_1+ 0.57))  + ", " + ("{:.2f}".format(final_answer_2+0.57))  + ")"
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand }
    return dict

def linear_medium():
    a = 1
    b = randint(1,4)
    c = randint(-4,-1)
    d = 3
    e = randint(1,4)
    f = randint(-5,-1)
    question = 'Solve the linear equations %sx + %sy = 0 and %sx + %sy + %s = 0' %(a,b,d,e,f)
    answer_1 = b*f
    answer_2 = e*c
    answer_3 = e*a
    answer_4 = b*d
    answer_5 = d*c
    answer_6 = f*a
    final_answer_1 = float(answer_1 - answer_2) / (answer_3 - answer_4)
    final_answer_2 = float(answer_5 - answer_6) / (answer_3 - answer_4)
    answer = "(" + "{:.2f}".format(final_answer_1) + ", " + "{:.2f}".format(final_answer_2) + ")"
    option1 = "(" + ("{:.2f}".format(final_answer_1+ 0.34))  + ", " + ("{:.2f}".format(final_answer_2+0.34))  + ")"
    option2 = "(" + ("{:.2f}".format(final_answer_1+ 0.53))  + ", " + ("{:.2f}".format(final_answer_2+0.53))  + ")"
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand }
    return dict

def linear_hard():
    a = randint(13,20)
    b = randint(1,7)
    c = randint(5,10)
    d = randint(2,7)
    e = randint(4,8)
    f = randint(12,20)
    question = 'Solve the linear equations %sx + %sy = 0 and %sx + %sy + %s = 0' %(a,b,d,e,f)
    answer_1 = b*f
    answer_2 = e*c
    answer_3 = e*a
    answer_4 = b*d
    answer_5 = d*c
    answer_6 = f*a
    final_answer_1 = float(answer_1 - answer_2) / (answer_3 - answer_4)
    final_answer_2 = float(answer_5 - answer_6) / (answer_3 - answer_4)
    answer = "(" + "{:.2f}".format(final_answer_1) + ", " + "{:.2f}".format(final_answer_2) + ")"
    option1 = "(" + ("{:.2f}".format(final_answer_1+ 0.3))  + ", " + ("{:.2f}".format(final_answer_2+0.3))  + ")"
    option2 = "(" + ("{:.2f}".format(final_answer_1+ 0.4))  + ", " + ("{:.2f}".format(final_answer_2+0.4))  + ")"
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand }
    return dict

def easy_addition():
    a = randint(1, 20)
    b = randint(1, 20)
    question = 'Add the numbers ' + str(a) + ' and ' + str(b)
    answer = a + b
    option1 = answer + randint(5, 8)
    option2 = answer + randint(3, 5)
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand , 'param1' : a , 'param2' : b }
    return dict

def easy_subtraction():
    a = randint(20,50)
    b = randint(1,20)
    question = 'Subtract the numbers' + str(a) + ' and ' + str(b)
    answer = a - b
    option1 = answer - randint(1,3)
    option2 = answer + randint(3,5)
    option3 = answer - randint(5,7)
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand , 'param1' : a , 'param2' : b }
    return dict

def easy_multiply():
    a = randint(1,20)
    b = randint(1,20)
    question = 'Multiply the numbers' + str(a) + ' and ' + str(b)
    answer = a * b
    option1 = answer - randint(1,3)
    option2 = answer + randint(3,5)
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand , 'param1' : a , 'param2' : b }
    return dict

def easy_divide():
    a = randint(1,20)
    b = randint(40,60)
    answer = b/a
    question = 'Divide the numbers' + str(a) + ' and ' + str(b)
    while(b%a != 0):
        answer = b/a
        a = a + 1
    option1 = answer - randint(1,3)
    option2 = answer + randint(3,5)
    array = [option1 , option2]
    array.insert(answer, randint(0,2))
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand , 'param1' : a , 'param2' : b }
    return dict

def medium_operation():
    dic_add = easy_addition()
    dic_sub = easy_subtraction()
    question = 'Solve the  expression ' + str(dic_add['param1'])  + ' + ' + str(dic_add['param2']) + ' - ' + str(dic_sub['param1']) + ' - ' + str(dic_sub['param2'])
    answer = dic_add['param1'] + dic_add['param2'] - dic_sub['param1'] - dic_sub['param2']
    param1 = dic_add['param1'] + dic_add['param2']
    param2 = dic_sub['param1'] - dic_sub['param2']
    option1 = answer + randint(1,3)
    option2 = answer + randint(3,5)
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand , 'param1' : param1 , 'param2' : param2 }
    return dict

def advacned_operation():
    dic_mult = easy_multiply()
    dic_div = easy_divide()
    dic_add = easy_addition()
    dic_sub = easy_subtraction()
    question = 'Solve the expression ( %s + %s )  + ( %s - %s ) + ( %s * %s ) + ( %s / %s )' %(dic_add["param1"], dic_add['param2'],dic_sub['param1'],dic_sub['param2'],dic_mult['param1'],dic_mult['param2'],dic_div['param1'],dic_div['param2'])
    answer = (int(dic_add['param1']) + int(dic_add['param2'])) + (int(dic_sub['param1']) - int(dic_sub['param2'])) + (int(dic_mult['param1']) * int(dic_mult)['param2']) + ( int(dic_div['param1'])/int(dic_div['param2']) )
    option1 = answer + 3
    option2 = answer + 5
    array = [option1 , option2]
    rand = randint(0,2)
    array.insert(rand, answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : rand , 'param1' : param1 , 'param2' : param2 }
    return dict
