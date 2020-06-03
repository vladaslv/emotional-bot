import requests
from flask import Flask, request

from .credentials import ACCESS_TOKEN, VERIFY_TOKEN
from .const import GRAPH_URL
from .bot import Bot

app = Flask(__name__)
sensitive_bot = Bot()

@app.route('/', methods=['GET'])
def handle_verification():
    #  Verificate token related to callback URL set on fb
    token_sent = request.args.get('hub.verify_token')
    return verify_fb_token(token_sent)

@app.route('/', methods=['POST'])
def handle_messages():
    #  Get message sent from user
    output = request.get_json()
    for event in output['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message'):
                sender_id = message['sender']['id']
                if message['message'].get('text'):
                    send_message(message['message']['text'], sender_id)
    return 'ok'

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def send_message(text, sender_id):
    feedback_message = sensitive_bot.handle_user_message(text)
    request_body = {
        'recipient': {
            'id': sender_id
        },
        'message': {"text":feedback_message}
    }
    response = requests.post(
        GRAPH_URL+ACCESS_TOKEN,
        json=request_body
    ).json()
    return response