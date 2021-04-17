import telebot
from keyboards import keyboard_colors
from readwrite import get_id_and_token, get_ids_to_send, log_str
from infostrings import colors_question_string

token, my_id = get_id_and_token()
bot = telebot.TeleBot(token)

user_ids = get_ids_to_send()
for user_id in user_ids:
    try:
        bot.send_message(user_id, colors_question_string, reply_markup=keyboard_colors)
        log_str(f'user_id: {user_id}   sent question about colors to user\n')
    except Exception as e:
        log_str(str(e) + '\n')
