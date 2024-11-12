import telebot

token = '7901226820:AAHym0_yX9eG4yrN6xk37e39OvOXiU1IoF4'

bot = telebot.TeleBot(token)

my_name = 'Андрей'

@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        text = 'Ба! Знакомые все лица!'
    else:
        text = message.text
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)