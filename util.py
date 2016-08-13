import json
import requests
from constants import SEND_MESSAGE_URL, PAT as token

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
          params = {'access_token' : token},
          data = json.dumps({
              "recipient" : {"id" : recipient},
              "message" : {
                  "attachment" : {
                  "type" : "template",
                  "payload" : {
                      "template_type" : "button",
                      "text" : text,
                      "buttons" : buttons
                  }
              }}
          }),
          headers={'Content-type': 'application/json'})
    print r.text


def generate_button(text, payload = None, type="text", url = None):
    if type == "url":
        return {
            "type" : "web_url",
            "url" : text,
            "title" : text
        }
    else:
        return {
            "type" : "postback",
            "title" : text,
            "payload" : payload
        }

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
    if "message" in event and "text" in event["message"]:
        return (event["sender"]["id"], event["message"]["text"].encode('unicode_escape'))
    elif "postback" in event and "payload" in event["postback"]:
        return (event["sender"]["id"], event["postback"]["payload"])
