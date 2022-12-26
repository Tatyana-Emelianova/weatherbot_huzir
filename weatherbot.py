import telebot
# import requests
from pyowm import OWM
from pyowm.utils.config import get_default_config
# config_dict = get_default_config()  почему то не работает перевод на русский словарь
# config_dict['language'] = 'ru'

code_smile = {
        "Clear": "Ясно \U0001F600",
        "Clouds" : "Облачно \U0001F642",
        "Rain": "Дождь \U0001F610",
        "Drizzle": "Дождь \U0001F610",
        "Thunderstorm": "Гроза \U0001F636",
        "Snow": "Снег \U0001F636",
        "Mist": "Туман \U0001F636",

    }

owm = OWM ("ac4c7c196d18c8da5e47f37359c49f82")
place = "Хужир" #input ('введите город ')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
t = w.temperature("celsius")
t1 = t["temp"]
t2 = t["feels_like"]
t3 = t["temp_max"]
t4 = t["temp_min"]
st = w.status
if st in code_smile:
    emoji_st = code_smile[st]
else:
    emoji_st = w.status


token = "TOKEN"
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['weather'])
def start_message(message):
    mes = (f' Погода в Ольхонском районе: \n{emoji_st}\nтемпература сейчас: {t1} °C'
    f'\nощущается как: {t2} °C \nминимальная за сутки: {t3} °C \nмаксимальная за сутки: {t4} °C'
    f'\n ***\U0001F600 Хорошего дня! \U0001F600***')
    bot.send_message(message.chat.id, mes)


bot.infinity_polling()
