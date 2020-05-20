import config
import telebot
from datetime import timedelta, datetime
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'бла-бла-бла', reply_markup=keyboard())

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # реакция на текстовые сообщения
    now = datetime.now()    #определение времени в иркутске
    nowIKT = now + timedelta(hours=8)
    if message.text == "🕙Время": # Если сообщение "Время" тогда выполняем
        bot.send_message(message.chat.id, datetime.strftime(nowIKT, "%H:%M:%S\n%d.%m.%Y"))# Отправляем ответ на сообщение
    elif message.text == "🏄Отпуск": # Если сообщение "Отпуск" тогда выполняем
        vacation = datetime(2020,7,18,17,00) - nowIKT # Вычисляем количество(!) времени ДО отпуска
        mm, ss = divmod(vacation.seconds, 60)         # Разделяем количество времени на дни, часы, минуты и секунды
        hh, mm = divmod(mm, 60)
        bot.send_message(message.chat.id, 'До отпуска {} дней {} часа {} мин {} сек.'.format(vacation.days, hh, mm, ss))
                                                                                        # Отправляем ответ на сообщение
    else:
        bot.send_message(message.chat.id, "Моя твоя не понимать") # Отправляем ответ на сообщение

def keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('🏄Отпуск')
    btn2 = types.KeyboardButton('🕙Время')
    markup.add(btn1,btn2)
    return markup

if __name__ == '__main__':#постоянно смотрим в чат
    bot.polling(none_stop=True)