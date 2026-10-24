import telebot
import os

# Считываем токен из переменных Amvera
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Йоу! Бот успешно запущен и работает в облаке Amvera! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написала: {message.text}")

if __name__ == '__main__':
    bot.infinity_polling()
