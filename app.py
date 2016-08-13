from flask import Flask, request
import requests
import json
import traceback
import random
from constants import *
import os

app = Flask(__name__)

@app.route('/webhook')
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.verify_token')
        else:
            return "It's working well"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host = "0.0.0.0",port = port)
