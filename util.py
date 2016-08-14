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

def advacned_operation():
	dic_mult = easy_multiply()
	dic_div = easy_divide()
	dic_add = easy_addition()
	dic_sub = easy_subtraction()
	question = 'Solve the expression ( %s + %s )  + ( %s - %s ) + ( %s * %s ) + ( %s / %s )' %(dic_add["param1"], dic_add['param2'],dic_sub['param1'],dic_sub['param2'],dic_mult['param1'],dic_mult['param2'],dic_div['param1'],dic_div['param2']) 
	answer = (int(dic_add[param1]) + int(dic_add[param2])) + (int(dic_sub[param1]) - int(dic_sub[param2])) + (int(dic_mult[param1]) * int(dic_mult)[param2]) + ( int(dic_div[param1])/int(dic_div[param2]) )
	option1 = answer + 3
	option2 = answer + 5
	option3 = answer + 8
	array = [option1 , option2]
    array.insert(randint(0,2), answer)
    dict = { 'question': question , 'option1' : array[0] , 'option2' : array[1] , 'option3' : array[2] , 'answer' : str(answer) , 'param1' : param1 , 'param2' : param2 }
    return dict
	#question = 'Solve the expression ' + str(med_add['param1']) + ' + '+  str(med_add['param2']) 
	#return question	


def linear_easy():
	a = randint(4,6)
	b = 1
	c = 1
	d = randint(1,4)
	e = randint(1,4)
	f = randint(5,10)
	question = 'Solve the linear equations %sx + %sy = 0 and %sx + %sy + %s = 0' %(a,b,d,e,f)
	answer_1 = b*f
	answer_2 = 0 #e*c
	answer_3 = e*a
	answer_4 = b*d
	answer_5 = 0 #d*c
	answer_6 = f*a
	final_answer_1 = float(answer_1 - answer_2) / (answer_3 - answer_4)
	final_answer_2 = float(answer_5 - answer_6) / (answer_3 - answer_4)
	answer = "(" + "{:.2f}".format(final_answer_1) + ", " + "{:.2f}".format(final_answer_2) + ")"
	option1 = "(" + ("{:.2f}".format(final_answer_1+ 0.23))  + ", " + ("{:.2f}".format(final_answer_2+0.23))  + ")"
	option2 = "(" + ("{:.2f}".format(final_answer_1+ 0.57))  + ", " + ("{:.2f}".format(final_answer_2+0.57))  + ")"
	option3 = "(" + ("{:.2f}".format(final_answer_1+ 0.73))  + ", " + ("{:.2f}".format(final_answer_2+0.73))  + ")"
	dict = {'question' : question, 'answer' : answer, 'option1' : option1,'option2' : option2,'option3' : option3}
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
	option3 = "(" + ("{:.2f}".format(final_answer_1+ 0.77))  + ", " + ("{:.2f}".format(final_answer_2+0.77))  + ")"
	dict = {'question' : question, 'answer' : answer, 'option1' : option1,'option2' : option2,'option3' : option3, 'param1' : a , 'param2' : b, 'param3' : c, 'param4' : d, 'param5' : e, 'param6' : f}
	return dict

def linear_hard():
	a = randint(1,5)
	b = randint(1,5)
	c = randint(2,10)
	d = randint(1,5)
	e = randint(1,5)
	f = randint(1,5)
	question = 'Solve the linear equations %sx + %sy = 0 and %sx + %sy + %s = 0' %(a,b,d,e,f)
	answer_1 = b*f
	answer_2 = 0 #e*c
	answer_3 = e*a
	answer_4 = b*d
	answer_5 = 0 #d*c
	answer_6 = f*a
	final_answer_1 = float(answer_1 - answer_2) / (answer_3 - answer_4)
	final_answer_2 = float(answer_5 - answer_6) / (answer_3 - answer_4)
	answer = "(" + "{:.2f}".format(final_answer_1) + ", " + "{:.2f}".format(final_answer_2) + ")"
	option1 = "(" + ("{:.2f}".format(final_answer_1+ 0.3))  + ", " + ("{:.2f}".format(final_answer_2+0.3))  + ")"
	option2 = "(" + ("{:.2f}".format(final_answer_1+ 0.4))  + ", " + ("{:.2f}".format(final_answer_2+0.4))  + ")"
	option3 = "(" + ("{:.2f}".format(final_answer_1+ 0.5))  + ", " + ("{:.2f}".format(final_answer_2+0.5))  + ")"
	dict = {'question' : question, 'answer' : answer, 'option1' : option1,'option2' : option2,'option3' : option3, 'param1' : a , 'param2' : b, 'param3' : c, 'param4' : d, 'param5' : e, 'param6' : f}
	return dict

'''
def quad_easy(): 


def quad_medium(): 


def quad_expert():

def trigo_easy(): 

def trigo_medium(): 

def trigo_hard():  
'''