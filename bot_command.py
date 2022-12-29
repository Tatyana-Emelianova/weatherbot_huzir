import telebot
from telebot import types

import pyowm
from pyowm import OWM
import tokenn as t
owm = OWM(t.api())
# from view import an



def starting():
        # Добавляем кнопки
        markup=types.ReplyKeyboardMarkup(row_width=1)
        item1=types.KeyboardButton("Актуальный набор")
        item2=types.KeyboardButton("записать на тур")
        item3=types.KeyboardButton("заявка на тур")
        markup.add(item1, item2, item3)
        return markup


def numbers():
        markup=types.ReplyKeyboardMarkup(row_width=4)
        item1=types.KeyboardButton("1")
        item2=types.KeyboardButton("2")
        item3=types.KeyboardButton("3")
        item4=types.KeyboardButton("4")
        item5=types.KeyboardButton("5")
        item6=types.KeyboardButton("6")
        item7=types.KeyboardButton("7")
        item8=types.KeyboardButton("8")
        item9=types.KeyboardButton("9")
        item10=types.KeyboardButton("10")
        item11=types.KeyboardButton("11")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
        # for i in range(1, 12):
        #         item=types.KeyboardButton(f"{i}")
        #         markup.add(item)
        return markup

def act_list(name):
        listt = actual_open(name).split('\n')
        newlist = []
        for i in listt:
                a = i.split()
                newlist.append(a)
        return newlist


def datbutton(data_file):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        newlist = act_list(data_file)
        # newlist = act_list('act_recruiting')
        for item in newlist:
                markup.add(types.KeyboardButton(f"{item[0]}"))
        return (markup)

# def regbutton():
#         markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#         newlist = act_list('trips')
#         for item in newlist:
#                 markup.add(types.KeyboardButton(f"{item[0]}"))
#         return (markup)



def actual_open (name):
        with open(f'{name}.txt', 'r', encoding='UTF-8') as f:
                act_rec  = f.read()
                return act_rec

# def dating_count(trip):
#         newlist = act_list('act_recruiting')
#         for item in newlist:
#                 if trip == item[0]:
#                         tripdate = trip
#                         tripdate 
#                         return item[1]


def dating_count(trip, data_file):
        newlist = act_list(data_file)
        for item in newlist:
                if trip == item[0]:
                        return item                      

def requests_count(trip):
        newlist = act_list('trips')

        for item in newlist:
                if trip == item[0]:
                        tripreg = trip
                        tripreg
                        return item[1]

def writing(i, first_name):
        
        print(b)
        if b[0] != None:
                with open(f'data.txt', 'a', encoding='UTF-8') as f:
                        f.write(f'{b[0]} - {i} человек от {first_name}')
                
                listt = act_list('act_recruiting')
                newlistact = []
                new = ''
                for item in listt:
                        if b[0] == item[0]:
                                item[1] = int(item[1]) - int(i)
                                str(item[1])
                                new = ''.join(item)
                        else:
                                new = ''.join(item)
                        newlistact.append(new)
                        new = ''
                new = '\n'.join(newlistact)
                with open(f'act_recruiting.txt', 'w', encoding='UTF-8') as f:
                        f.write(new)
                return "ок"
        # elif tripreg != None:
        #         with open(f'requests.txt', 'a', encoding='UTF-8') as f:
        #                 f.write(f'{tripdate} - {i} человек от {first_name}')
                               
        #         return "ок"
        else:
                return 'не ок'



def weather_mes():
        code_smile = {
        "Clear": "Ясно \U0001F600",
        "Clouds" : "Облачно \U0001F642",
        "Rain": "Дождь \U0001F610",
        "Drizzle": "Дождь \U0001F610",
        "Thunderstorm": "Гроза \U0001F636",
        "Snow": "Снег \U0001F636",
        "Mist": "Туман \U0001F636",
        }

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
        cl = w.clouds
        wi = w.wind()["speed"]
        if st in code_smile:
            emoji_st = code_smile[st]
        else:
            emoji_st = w.status

        mes = (f' Погода в Ольхонском районе: \n{emoji_st}\nтемпература сейчас: {t1} °C'
        f'\nощущается как {t2} °C \nветер: {wi} м/с \nоблачность {cl} % '
        f'\n ***\U0001F600 Хорошего дня! \U0001F600***')

        return mes