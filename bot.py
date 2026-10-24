import telebot
import os
from telebot import types

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
user_states = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(types.KeyboardButton('🔍 Лор прокрастинации (Почему мы NPC?)'), 
               types.KeyboardButton('📅 Идеальное блочное расписание'), 
               types.KeyboardButton('💡 Базированные лайфхаки'), 
               types.KeyboardButton('🎮 Сделать тест и собрать свой график'))
    bot.send_message(message.chat.id, f"Йоу, {message.from_user.first_name}! 👋\nДобро пожаловать в хаб прокачки времени!", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    chat_id = message.chat.id
    if message.text == '🔍 Лор прокрастинации (Почему мы NPC?)':
        bot.send_message(chat_id, "🧬 **Лор прокрастинации:** Каждые 5 минут в соцсетях выжигают дофамин. Из-за этого ты прокрастинируешь.")
    elif message.text == '📅 Идеальное блочное расписание':
        bot.send_message(chat_id, "📅 **Конструктор дня:** Используй гибкие фокус-блоки вместо душных планов!")
    elif message.text == '💡 Базированные лайфхаки':
        bot.send_message(chat_id, "⚡ **Лайфхаки:** Цифровой детокс и метод Помодоро (45 минут работы / 15 отдыха).")
    elif message.text == '🎮 Сделать тест и собрать свой график':
        user_states[chat_id] = {}
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("А) С утра ☀️", callback_data="quiz_q1_a"),
                   types.InlineKeyboardButton("Б) Ближе к вечеру 🌙", callback_data="quiz_q1_b"))
        bot.send_message(chat_id, "🎮 **Вопрос 1/3: Когда твой мозг выдает пик продуктивности?**", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("quiz_"))
def handle_advanced_quiz(call):
    chat_id = call.message.chat.id
    bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=None)
    bot.send_message(chat_id, "📊 **Анализ завершен!** Внедряй технику *Помодоро* и начни могать лени! 🔥")

if __name__ == '__main__':
    bot.infinity_polling()

