import telebot
from telebot import types
from functions import getTemeratureCity
from functions import  parseGetCity

def parseStringForSum(str):
    sum = 0
    currentNum = ''
    for i in range(len(str)):
        if str[i].isdigit():
            currentNum+=str[i]
        elif (str[i].isdigit()==False and len(currentNum)>0):
            sum+=int(currentNum)
            currentNum=''

    sum+=int(currentNum)
    return sum




TOKEN = '6074825758:AAHJ_h_GwPSbQ0_-_l-CcPBpQaLSoFzyFbg'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.from_user.id,'Привет, ' + str(message.from_user.username))


@bot.message_handler(content_types=['text'])
def getTextMessage(message):
    if message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'у меня все отлично')

    elif message.text == 'sliv':
        bot.send_message(message.from_user.id, 'вау, ты знаешь что-то особенное, держи подарок www.amazon.com')


    elif 'сложи числа' in message.text:
        bot.send_message(message.from_user.id, (parseStringForSum(message.text)))

    elif 'temp' in message.text:
        bot.send_message(message.from_user.id, getTemeratureCity(parseGetCity(message.text)))

bot.polling(none_stop=True,interval = 0)

