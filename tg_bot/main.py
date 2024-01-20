#  Copyright (c) ChernV (@otter18), 2021.
import string
import os
import random
import telebot
import requests

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))
api_link = "https://012c-188-233-65-224.ngrok-free.app"

# ---------------- dialog params ----------------
dialog = {
    'hello': {
        'in': ['/hello', 'привет', 'hello', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    'how r u': {
        'in': ['/howru', 'как дела', 'как ты', 'how are you', 'дела', 'how is it going'],
        'out': ['Хорошо', 'Отлично', 'Good. And how are u?']
    },
    'name': {
        'in': ['/name', 'зовут', 'name', 'имя'],
        'out': [
            'Я telegram-template-bot',
            'Я бот шаблон, но ты можешь звать меня в свой проект'
        ]
    }
}

def remove_punctuation(text):
            text = text.translate(str.maketrans('', '', '[]\''))
            return text

# --------------------- bot ---------------------
@bot.message_handler(commands=['synonims'])
def synonyms(message):
    response = requests.get(api_link + '/api/v1.0/page-info/' + message.text.lower()[10:])
    if response.status_code==500:
        bot.send_message(message.chat.id,
        "Ой, кажется, что-то пошло не так",
        parse_mode='markdown')
        return
    else:
        syn_text = ''
        for item in response.json()['synonyms']:
            syn_text += ('\n - ' + remove_punctuation(str(item)) + ': ' + remove_punctuation(str(response.json()['synonyms'][item])))

@bot.message_handler(func=lambda message: True)
def test(message):
    response = requests.get(api_link + '/api/v1.0/page-info?page-addr='+message.text)
    if response.status_code==404:
        bot.send_message(message.chat.id,
            "**Неверный формат ввода. Отправьте ссылку на новость блокнот-волгоград **",
            parse_mode='markdown')
    elif response.status_code==500:
            bot.send_message(message.chat.id,
            "Ой, кажется, что-то пошло не так",
            parse_mode='markdown')
            return
    else:
        response = response.json()
        bot.send_message(message.chat.id,
            "*Заголовок: *" + response['title'] + '\n\n' +
            "*Дата: *" + response['date'] +'\n\n' +
            "*Ссылка: *" + message.text + '\n\n' +
            "*Текст: *" + response['text'],
            parse_mode='markdown')

        response = requests.get(api_link + '/api/v1.0/page-info/vip-persons')
        if response.status_code==404:
            vip_text = "VIP-персоны не найдены"
        elif response.status_code==500:
            bot.send_message(message.chat.id,
            "Ой, кажется, что-то пошло не так",
            parse_mode='markdown')
            return
        else:
            vip_text = ''
            for item in response.json()['vip_persons']:
                vip_text += ('\n - ' + item)
        response = requests.get(api_link + '/api/v1.0/page-info/sights')
        if response.status_code==404:
            sights_text = "Достопримечательности не найдены"
        elif response.status_code==500:
            bot.send_message(message.chat.id,
            "Ой, кажется, что-то пошло не так",
            parse_mode='markdown')
            return
        else:
            sights_text = ''
            for item in response.json()['sights']:
                remove_punctuation(str(item))
                sights_text += ('\n - ' + item)
            
        bot.send_message(message.chat.id,
            "*VIP персоны: *" + vip_text + '\n\n' +
            "*Достопримечательности: *" + sights_text,
            parse_mode='markdown')
    
        response = requests.get(api_link + '/api/v1.0/page-info/summarized')
        if response.status_code==500:
            bot.send_message(message.chat.id,
            "Ой, кажется, что-то пошло не так",
            parse_mode='markdown')
            return
        else:
            response = response.json()
            summ_text = response['summarized']

    #    response = requests.get(api_link + '/api/v1.0/page-info/rewrited')
    #    if response.status_code==500:
    #        bot.send_message(message.chat.id,
    #        "Ой, кажется, что-то пошло не так",
    #        parse_mode='markdown')
    #        return
    #    else:
    #        rewr_text = ''
    #        rewr_text += response.json()['rewrited']
        
        response = requests.get(api_link + '/api/v1.0/page-info/sentiment')
        if response.status_code==500:
            bot.send_message(message.chat.id,
            "Ой, кажется, что-то пошло не так",
            parse_mode='markdown')
            return
        else:
            sentiment_text = ''
            for item in response.json()['sentiments']:
                sentiment_text += ('\n - ' + remove_punctuation(str(item)) + ': ' + remove_punctuation(str(response.json()['sentiments'][item])))
        
        bot.send_message(message.chat.id,
            "*Аннотация: *" + summ_text + '\n\n' +
    #        "*Рерайт: *" + rewr_text + '\n\n' +
            "*Тональность: *" + sentiment_text,
            parse_mode='markdown')
        
    #    response = requests.get(api_link + '/api/v1.0/page-info/common-words')
    #    if response.status_code==500:
    #        bot.send_message(message.chat.id,
    #        "Ой, кажется, что-то пошло не так",
    #        parse_mode='markdown')
    #        return
    #    else:
    #        c_words = response.json()
    #        c_words_text = ''
    #        for item in response.json()['words']:
    #            remove_punctuation(str(item))
    #            c_words += ('\n - ' + item)
    #    bot.send_message(message.chat.id,
    #        "*Часто встречающиеся слова: *" + c_words,
    #        parse_mode='markdown')
        

# ---------------- local testing ----------------
if __name__ == '__main__':
    bot.infinity_polling()
