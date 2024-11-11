# импорт библиотек
import telebot
from pyexpat.errors import messages
import webbrowser
from telebot import types
from dotenv import load_dotenv
import os
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# назначение переменной и токен бота
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Перейти на сайт",)
    markup.row(btn1)
    btn2 = types.KeyboardButton("уничтожить фото", )
    btn3 = types.KeyboardButton("что-то интересное", )
    markup.row(btn2, btn3)
    file = open('./for tg starter tg bot.jpg', "rb")
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "Перейти на сайт":
        webbrowser.open("https://ru.pinterest.com/pin/8655424280835592/")
    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id, "deleted")


# обработка фото с кнопками
@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на сайт", url="https://ru.pinterest.com/pin/563018697274866/")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("уничтожить фото",callback_data="delete")
    btn3 = types.InlineKeyboardButton("что-то интересное", callback_data="edit")
    markup.row(btn2, btn3)
    bot.reply_to(message, "замечательно", reply_markup=markup)

# функция для работы кнопок
@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    if callback.data == "edit":
        bot.edit_message_text("Выбора больше нет)", callback.message.chat.id, callback.message.message_id)


# команда перехода на вебсайт
@bot.message_handler(commands=["site"])
def send_site(message):
    webbrowser.open("https://ru.pinterest.com/pin/563018697274872/")

# команда start


# команда help
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "<b>Данный бот создан для обучения</b>",parse_mode='html')

#  ответы на сообщения привет и id
@bot.message_handler()
def text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}")
    elif message.text.lower() == "id":
        bot.reply_to(message, f"ID: {message.from_user.id}")

# команда позволяющая боту работать бесконечно
bot.polling(non_stop= True)
# внесены изменения в расположение проекта 