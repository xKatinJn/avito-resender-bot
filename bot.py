import os
import logging

from database import Chat

from localization import messages_loc

from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, CallbackContext, Filters


API_TOKEN = os.getenv('BOT_API_TOKEN')

bot = Bot(token=API_TOKEN)


def message_handler(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    current_chat = update.message.chat
    bot_info = bot.get_me()
    print(f'User msg is: "{text}"')
    if current_chat['type'] in ['group', 'supergroup']:
        chat_id = int(current_chat['id'])
        if text in ['/start', f'/start@{bot_info.username}']:
            for chat in Chat.get_all_chats():
                print(f'CHAT = {chat}')
                if chat['is_active']:
                    bot.send_message(chat_id, messages_loc['bot_currently_registered'])
                    return
            new_active_chat = Chat(chat_id=chat_id, is_active=True)
            new_active_chat.save()
            bot.send_message(chat_id, messages_loc['bot_started'])
        elif text in ['/end', f'/end@{bot.username}']:
            for chat in Chat.get_all_chats():
                if chat['is_active'] and chat['chat_id'] == chat_id:
                    Chat.delete_by_id(chat['id'])
                    bot.send_message(chat_id, messages_loc['bot_ended'])


def start() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    updater = Updater(
        token=API_TOKEN if API_TOKEN else open('token.txt', 'r').read().replace('\n', '').replace(' ', ''),
        use_context=True
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    start()
