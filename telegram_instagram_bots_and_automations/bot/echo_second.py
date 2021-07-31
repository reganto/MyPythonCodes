import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Press me", callable_data="press")],
    ])

    bot.sendMessage(chat_id, "Use inline keyboard", replay_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
    print("Callback Query:", query_id, from_id, query_data)

    bot.answerCallbackQuery(repla, text="Got it")


TOKEN = sys.argv[1]
bot = telepot.Bot(TOKEN)

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
                
print('Listening ...')

while True:
    time.sleep(10)
