import telebot
from telebot import types


my_token = '5017505479:AAFhKcFFVFKaa4d42u9xw8XBm1ixRxsTlgk'
bot = telebot.TeleBot(my_token)

master_id = 403736985

name = ''
surname = ''
age = 0
id = 0

names = []
surnames = []
ages = []
ids = []

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        id = message.from_user.id
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): # получаем имя
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message): # получаем имя фамилию
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message): # получаем возраст
    global age
    age = int(message.text)
    # bot.send_message(message.from_user.id, 'Тебя зовут {} {} и тебе {}?'.format(name, surname, age))

    keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');  # кнопка «Да»
    keyboard.add(key_yes);  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Тебя зовут {} {} и тебе {}?'.format(name, surname, age)
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        names.append(name)
        surnames.append(surname)
        ages.append(age)
        ids.append(id)
        # код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Будем знакомы!')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Вот ведь незадача...')
        bot.send_message(master_id, 'Пиздит кто-то!')
        # переспрашиваем



bot.polling(none_stop=True, interval=5)
