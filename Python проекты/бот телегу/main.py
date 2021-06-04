import telebot
import config
import random

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def welcome (message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Шо тут забыл?")
    
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, "Здарова Чел,\n Я - <b>{1.first_name}</b>, Тестовая фигня программиста дебилоида".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def povtor (message):
    if message.chat.type == 'private':
        if message.text == 'Шо тут забыл?':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Шо тут забыл?':
            bot.send_message(message.chat.id, 'Да ниче')
        else:
            bot.send_message(message.chat.id, 'Ну чё стоишь тогда как не родной? иди нах от сюда')
    
bot.polling(none_stop = True)