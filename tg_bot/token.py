import telebot
bot = telebot.TeleBot("6714031388:AAGu0vAFIsJ1c0Y8QPvlG-IDPl0bn6a9V60")

bot.remove_webhook()
bot.set_webhook("https://d5denvdmv3fj9825hemd.apigw.yandexcloud.net")
