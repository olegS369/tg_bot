import telebot
import random, os

from funk_bot import *
bot = telebot.TeleBot("????????????????????")

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("hello", "hello")
        #telebot.types.BotCommand("exxo 2", "exxoexxo")
    ],
    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
)


# Обработчик команды '/start' и '/hello'

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=['porol'])
def por(message):
    password = gen_pass(10)
    bot.reply_to(message, f"Генератор паролей активирован! вот твой пороль: {password}")

@bot.message_handler(commands=['randomaizer'])
def rand(message):
    bot.reply_to(message, "1 или 2, вот результат:")
    r_h(1, 2)

@bot.message_handler(commands=['photo'])
def send(message):
    file = random.choice(os.listdir('images'))
    with open(f'images/{file}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['eco'])
def eko(message):
    try:
        material = message.text.split()[1]
        answer = decomposition(material)
        bot.reply_to(message, 'срок разложения:')
        bot.reply_to(message, f'{answer}')
    except:
        bot.reply_to(message, 'попробуйте ввести в формате /eco материал еслине вышло попробуйте другой материал')
        

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    try:
        count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
        bot.reply_to(message, message.text * count_heh)
    except:
        bot.reply_to(message, 'попробуйте ввести в формате что-то число')

# Запуск бота
bot.polling()
