
# Надо загрузить библиотеку командой "pip install pytelegrambotapi"
# Надо загрузить библиотеку погоды командой "pip install pyowm"
import tokenn as t
import telebot

from telebot import types
import time

# import pyowm
# from pyowm import OWM

import bot_command as bc



bot = telebot.TeleBot(t.token())
# owm = OWM(t.api())



@bot.message_handler(commands=["start"])
# Получение сообщений от юзера
def start(message):
        bot.send_message(message.chat.id, 'Нажми: \n"Актуальный набор" для получения информации о набираемых турах и свободных местах\nзаписать на тур — для записи туриста на тур(только после оплаты/предоплаты)\n заявка на тур - для создания заявки на набор тура', reply_markup=bc.starting())


@bot.message_handler(commands=['weather'])
def weather(message):
    
    bot.send_message(message.chat.id, bc.weather_mes())


@bot.message_handler(content_types=["text"])
def handle_text(message):
    
    
    # an = bc.act_list("act_recruiting")

    an = bc.dating_count(message.text, 'act_recruiting')
    print(an)


    if message.text == 'Актуальный набор' :
        bot.send_message(message.chat.id, bc.actual_open('act_recruiting'))
        
        
    
    elif message.text == 'записать на тур' :
        bot.send_message(message.chat.id, 'На какой тур записываем?', reply_markup=(bc.datbutton("act_recruiting")))
        
        
        

    elif message.text == 'заявка на тур' :
        bot.send_message(message.chat.id, 'На какой тур заявку делаем?', reply_markup=(bc.datbutton("trips")))
        



    elif an != None:
        msg = bot.send_message(message.chat.id, f'Осталось только {an[1]}, сколько записываем?', reply_markup=(bc.numbers()))
        bot.register_next_step_handler(msg, process_count_step)
    def process_count_step(message):
        try:
            chat_id = message.chat.id
            name = message.text
            user = User(name)
            user_dict[chat_id] = user
            msg = bot.reply_to(message, 'How old are you?')
            bot.register_next_step_handler(msg, process_age_step)
        except Exception as e:
            bot.reply_to(message, 'oooops')

    
        
    # else:
    #     # an = bc.requests_count(message.text)
    #     # if an != None:
    #     #     bot.send_message(message.chat.id, f'Осталось только {an}, сколько записываем?', reply_markup=(bc.numbers()))
    #     print(message.text)
          
    #     if message.text in str(range(12)):
            
    #         bot.send_message(message.chat.id, bc.writing(message.text, message.from_user.first_name))
            
        
    #     else:
    #         bot.send_message(message.chat.id, "я не знаааааю что делать, начни сначала /start") 
    #         # bot.send_message(message.chat.id,'...', reply_markup=(bc.starting(message, False)))
     
    
    










# Запускаем бота
print('ok')
bot.polling(none_stop=True, interval=0)
