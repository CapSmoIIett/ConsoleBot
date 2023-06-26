import telebot

#file with token
file = open("token.txt", 'r')

# Add telegram token
bot = telebot.TeleBot(file.read())


@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, '<b>Hi</b>', parse_mode='html') 

@bot.message_handler()
def user_message(message):
    bot.send_message(message.chat.id, message, parse_mode='html')

bot.polling(none_stop=True)



