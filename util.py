import json
import requests
from constants import SEND_MESSAGE_URL, PAT as token
from random import randint
import random


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


def generate_carasol_items(text, image_url, payload, showbtns = True):
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
            "url": text,
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


def easy_addition():
    a = randint(1, 20)
    b = randint(1, 20)
    question = 'Add the numbers ' + str(a) + ' and ' + str(b)
    answer = a + b
    option1 = answer + randint(5, 8)
    option2 = answer + randint(3, 5)
    array = [option1, option2]
    array.insert(randint(0,2), answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : str(answer) , 'param1' : a , 'param2' : b }
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
    array.insert(randint(0,2), answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : str(answer) , 'param1' : a , 'param2' : b }
    return dict

def easy_multiply():
    a = randint(1,20)
    b = randint(1,20)
    question = 'Multiply the numbers' + str(a) + ' and ' + str(b)
    answer = a * b
    option1 = answer - randint(1,3)
    option2 = answer + randint(3,5)
    array = [option1 , option2]
    array.insert(randint(0,2), answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : str(answer) , 'param1' : a , 'param2' : b }
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
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : str(answer) , 'param1' : a , 'param2' : b }
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



def get_solution_from_wolfarmAlpha(question):
    url = "http://api.wolframalpha.com/v2/query"
    params = {"input" : question, "appid" : "Q7K5HX-2Y24EKLAQW", "format" : 'image,plaintext'}
    r = requests.get(url, params = params)
    import pdb; pdb.set_trace()
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
