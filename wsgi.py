import json

import localization
from bot import bot
from database import Chat

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request)
    return {'status_code': '200'}


@app.route('/notifications_webhook', methods=['POST'])
def notifications_webhook():
    active_chat_id = [chat['chat_id'] for chat in Chat.get_all_chats() if chat['is_active']]
    if active_chat_id:
        data = request.json
        text = data['payload']['value']['content']['text']
        print(data)
        bot.send_message(active_chat_id[0], localization.messages_loc['bot_new_msg'].format(text))
    payload = {'ok': True}
    response = jsonify(payload)
    response.status_code = 200

    return response


app.run(host='0.0.0.0', debug=True)
