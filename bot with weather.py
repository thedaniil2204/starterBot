import telebot
import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(token=TELEGRAM_TOKEN)
API = "a6d72bb89542f1c6c3d7786153812376"
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напиши название города")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f'Сейчас погода в этом городе: {data["main"]["temp"]}')
    else:
        bot.reply_to(message, "Город не найден")


bot.polling(none_stop=True)