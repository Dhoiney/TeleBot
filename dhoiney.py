import random
import os
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    PrefixHandler,
    Filters,
)

USER_TOKEN = "1303693610:AAFS80JPDFdkyEAZmUGq_h7GhFaOoRMhZvU"


def start(bot, context):
    bot.message.reply_text("Hi,pipka!")


def get_num(bot, context):
    bot.message.reply_text(str(random.random()))



def math(bot, context):
    value = " ".join(context.args)
    result = eval(value)
    bot.message.reply_text(result)


def message(bot, context):
    text = bot.message.text 
    count = len(text)
    bot.message.reply_text(str(count))


def help(bot, context):
    file_name = "help.txt" 
    with open(file_name, "r") as file:
       bot.message.reply_text(file.read())


def save_file(bot, context):
    file_name, text = context.args[0], " ".join(
        context.args[1:]
    )
    # file_name = context.args[0]
    # text = " ".join(context.args[1:])
    file = open(file_name, "w")
    res = file.write(text)
    bot.message.reply_text(str(res))
    file.close()


def upd_file(bot, context):
    file_name, text = context.args[0], " ".join(
        context.args[1:]
    )
    file = open(file_name, "a")
    res = file.write(text)
    bot.message.reply_text(str(res),end = '/n')
    file.close()


def create_file(bot, context):
    file_name, text = context.args[0], " ".join(
    context.args[1:]
    )
    file = open(file_name, 'x')
    res = file.write(text)
    bot.message.reply_text(str(res))
    file.close()

def read_file(bot, context):
    file_name = context.args[0]
    with open(file_name, "r") as file:
        bot.message.reply_text(file.read())


def run_bot():
    updater = Updater(USER_TOKEN,use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("math", math))
    dispatcher.add_handler(PrefixHandler("#", "num", get_num))
    dispatcher.add_handler(PrefixHandler("!", "save", save_file))
    dispatcher.add_handler(PrefixHandler("!", "read", read_file))
    dispatcher.add_handler(PrefixHandler("!", "update", upd_file))
    dispatcher.add_handler(PrefixHandler("!", "create", create_file))
    dispatcher.add_handler(MessageHandler(Filters.text, message))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    run_bot()
