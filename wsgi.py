from bot import bot
from database import Chat

from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request)
    return {'status_code': '200'}


@app.route('/notifications_webhook', methods=['GET', 'POST'])
def notifications_webhoot():
    if request.method == 'GET':
        active_chat_id = [chat['chat_id'] for chat in Chat.get_all_chats() if chat['is_active']]
        if active_chat_id:
            bot.send_message(active_chat_id[0], 'TEST_SERVER')
    return '200'


app.run(host='0.0.0.0', debug=True)
