import telebot

my_token = '5017505479:AAFhKcFFVFKaa4d42u9xw8XBm1ixRxsTlgk'
bot = telebot.TeleBot(my_token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "Let's":
        bot.send_message(message.from_user.id, "GO!")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет или пнх")
    elif message.text == "пнх":
        answer = 'сам ' + message.text
        bot.send_message(message.from_user.id, answer)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=10)
