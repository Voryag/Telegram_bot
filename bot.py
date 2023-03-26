import telebot
from FORMULS import FORMULS

#bot.send_photo(chat_id, photo=open('path', 'rb'))
TOKEN = '5153632088:AAG97xAMmpXe3wmaAItKuHvhzt2nqjtHYRg'
TANGENT = open('Photos/tangent.png', 'rb') # figur='Окружность', theme='Основные свойства касательных к окружности'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = f'Я тебя категорически приветствую, {message.from_user.first_name} \n' \
           f'Этот бот предназначен для нахождения величин по геометрическим формулам. \n' \
           f'Выберите фигуры: \n'
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    start = telebot.types.KeyboardButton('/start')
    for i in FORMULS:
        button = telebot.types.KeyboardButton(f'{i}')
        markup.add(button)

    markup.add(start)

    bot.send_message(
        text=text,
        chat_id=message.chat.id,
        parse_mode='html',
        reply_markup=markup,
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    ps = 'Бот заточен под то, ' \
         'что у юзера имеется необходимость ' \
         'в ознакомлении формул по своей фигуре. ' \
         'Введя данные, ему высылаются информация'

    bot.send_message(message.chat.id, ps)

@bot.message_handler(func= lambda message: True)
def send_inf(message):
    global figur
    if message.text in FORMULS:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        figur = message.text
        for i in FORMULS[message.text]:
            button = telebot.types.KeyboardButton(f'{i}')
            markup.add(button)

        bot.send_message(text='Выберите по какой теме хотите получить информацию:', chat_id=message.chat.id, reply_markup=markup)

    if message.text in FORMULS[figur]:
        bot.send_message(text=FORMULS[figur][message.text], chat_id=message.chat.id)

    if figur == 'Окружность' and message.text == 'Основные свойства касательных к окружности':
        bot.send_photo(message.chat.id, TANGENT)

bot.infinity_polling(none_stop=True)