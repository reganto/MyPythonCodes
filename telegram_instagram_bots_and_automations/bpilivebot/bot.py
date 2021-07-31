import requests
import telebot

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    msg = 'Hi! I am bpi bot\nmy commands is /bpidollar, /bpipound, /bpieuro :)'
    chat_id = message.chat.id
    bot.send_message(chat_id, msg)


@bot.message_handler(commands=['bpidollar'])
def bpidollar(message):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = response.json()
    chat_id = message.chat.id
    bot.send_message(chat_id, response['bpi']['USD']['rate']+' '+'$')


@bot.message_handler(commands=['bpipound'])
def bpipound(message):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = response.json()
    chat_id = message.chat.id
    bot.send_message(chat_id, response['bpi']['GBP']['rate']+' '+'£')


@bot.message_handler(commands=['bpieuro'])
def bpieuro(message):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = response.json()
    chat_id = message.chat.id
    bot.send_messagechat_id, response['bpi']['EUR']['rate']+' '+'€')


bot.polling()

