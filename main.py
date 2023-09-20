import telebot
import os
import sys
import subprocess

#pr = subprocess.Popen(['dir'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)



#file with token
file = open("token.txt", 'r')

# Add telegram token
bot = telebot.TeleBot(file.read())


@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, '<b>Hi</b>', parse_mode='html') 

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    command = message.text
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, encoding='utf-8')
        
        # Отправляем результат выполнения команды обратно пользователю
        bot.send_message(message.chat.id, f"Результат выполнения команды:\n```\n{result}```", parse_mode="Markdown")
    except subprocess.CalledProcessError as e:
        # В случае ошибки отправляем сообщение с ошибкой
        bot.send_message(message.chat.id, f"Ошибка выполнения команды:\n```\n{e.output}```", parse_mode="Markdown")


def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print("start")
    print(output.decode())
    print("end")
    return output.decode()



bot.polling(none_stop=True)





