import telepot
from telepot.loop import MessageLoop
from pprint import pprint

bot = telepot.Bot("")

# response = bot.getUpdates(offset=125898155)
# pprint(response)

def handle(msg):
    pprint(msg)

MessageLoop(bot, handle).run_as_thread()
