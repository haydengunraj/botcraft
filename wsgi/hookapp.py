import base64
import hashlib
import hmac
import json

import requests
from flask import Flask, request, Response, send_file

import settings
from helper import generate_suggestions

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the homepage"

@app.route('/static/<image_file>')
def image(image_file):
    file_name = "static/{}".format(image_file)
    return send_file(file_name)

@app.route('/webhook', methods=['POST'])
def webhook():
    expected_sig = base64.b16encode(hmac.new(settings.KIK_API_KEY.encode('utf-8'), request.data, hashlib.sha1).digest()).decode('utf-8')
    signature = request.headers.get('X-Kik-Signature')

    if expected_sig != signature:
        return Response(status=403)

    messages = request.get_json()["messages"]
    for message in messages:
        sender = message["from"]
        chat_id = message["chatId"]
        msg_type = message["type"]
        if msg_type == "start-chatting":
            requests.post(
                settings.KIK_MESSAGE_URL,
                auth=(settings.KIK_USERNAME, settings.KIK_API_KEY),
                headers={
                    'Content-Type': 'application/json'
                },
                data=json.dumps({
                    'messages': [
                        {
                            'to': sender,
                            'type': 'text',
                            'chatId': chat_id,
                            'body': 'Hi, I\'m BotCraft! Send me an item name and I\'ll send you the crafting recipe.'
                        }
                    ]
                })
            )
        elif msg_type == "text":
            text = message["body"]
            matches = generate_suggestions(text)
            if len(matches) == 0:
                requests.post(
                    settings.KIK_MESSAGE_URL,
                    auth=(settings.KIK_USERNAME, settings.KIK_API_KEY),
                    headers={
                        'Content-Type': 'application/json'
                    },
                    data=json.dumps({
                        'messages': [
                            {
                                'to': sender,
                                'type': 'text',
                                'chatId': chat_id,
                                'body': 'No matches found! Make sure you\'ve spelled the name correctly and that the recipe exists.'
                            }
                        ]
                    })
                )
            elif len(matches) == 1:
                filename = matches.values()[0]
                url = settings.WEBSERVER_BASE_URL + "/static/{}".format(filename)
                if ".gif" in filename:
                    image = {'to': sender, 'type': 'video', 'chatId': chat_id, 'videoUrl': url, 'loop': True, 'autoplay': True}
                else:
                    image = {'to': sender, 'type': 'picture', 'chatId': chat_id, 'picUrl': url}
                requests.post(
                    settings.KIK_MESSAGE_URL,
                    auth=(settings.KIK_USERNAME, settings.KIK_API_KEY),
                    headers={
                        'Content-Type': 'application/json'
                    },
                    data=json.dumps({
                        'messages': [
                            {
                                'to': sender,
                                'type': 'text',
                                'chatId': chat_id,
                                'body': 'One moment please...'
                            }
                        ]
                    })
                )
                requests.post(
                    settings.KIK_MESSAGE_URL,
                    auth=(settings.KIK_USERNAME, settings.KIK_API_KEY),
                    headers={
                        'Content-Type': 'application/json'
                    },
                    data=json.dumps({
                        'messages': [
                            image,
                            {
                                'to': sender,
                                'type': 'text',
                                'chatId': chat_id,
                                'body': 'Send me an item name and I\'ll send you the crafting recipe.'
                            }
                        ]
                    })
                )
            elif len(matches) > 20:
                requests.post(
                    settings.KIK_MESSAGE_URL,
                    auth=(settings.KIK_USERNAME, settings.KIK_API_KEY),
                    headers={
                        'Content-Type': 'application/json'
                    },
                    data=json.dumps({
                        'messages': [
                            {
                                'to': sender,
                                'type': 'text',
                                'chatId': chat_id,
                                'body': 'Your search returned too many possibilities! Please try a more specific item name.'
                            }
                        ]
                    })
                )
            else:
                possibilities = [m.title() for m in matches]
                suggestions = []
                for p in possibilities:
                    suggestions.append({ 'type': 'text', 'body': p })
                requests.post(
                    settings.KIK_MESSAGE_URL,
                    auth=(settings.KIK_USERNAME, settings.KIK_API_KEY),
                    headers={
                        'Content-Type': 'application/json'
                    },
                    data=json.dumps({
                        'messages': [
                            {
                                'body': 'I found {} matches. Please choose an item from the keyboard below.'.format(len(matches)),
                                'to': sender,
                                'type': 'text',
                                'chatId': chat_id,
                                'keyboards': [
                                    {
                                        'to': sender,
                                        'type': 'suggested',
                                        'responses': suggestions
                                    }
                                ]
                            }
                        ]
                    })
                )
        return Response(status=200)

if __name__ == '__main__':
    app.run(debug=True)
