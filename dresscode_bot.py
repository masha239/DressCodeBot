from collections import defaultdict

import telebot
from readwrite import *
from keyboards import *
from infostrings import *
from utils import check_info_string
from fieldnames import *


token, my_id = get_id_and_token()
bot = telebot.TeleBot(token)
colors_dict = defaultdict(list)
MAX_COLORS_CNT = 4


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.from_user.id, help_string)


@bot.message_handler(commands=['write'])
def please_ask(message):
    bot.send_message(message.from_user.id, give_me_question_string)
    bot.register_next_step_handler(message, send_question)


def send_question(message):
    save_message(message.from_user.id, message.text)
    bot.send_message(message.from_user.id, question_is_delivered_string)


@bot.message_handler(commands=['settings'])
def send_settings(message):
    user_id = message.from_user.id
    settings_dict, settings_string = get_settings(user_id)
    bot.send_message(message.from_user.id, settings_string)
    bot.send_message(message.from_user.id, wanna_change_string, reply_markup=keyboard_change_info)


@bot.message_handler(commands=['send_colors'])
def send_settings(message):
    user_id = message.from_user.id
    log_str(f'user_id: {user_id}   sent question about colors to user\n')
    bot.send_message(user_id, colors_question_string, reply_markup=keyboard_colors)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    save_user(message.from_user.id)
    bot.send_message(message.from_user.id, welcome_string)
    bot.send_message(message.from_user.id, help_string)
    bot.send_message(message.from_user.id, give_me_timezone_string)
    bot.register_next_step_handler(message, get_timezone)
    log_str(f'user_id: {message.from_user.id}   NEW USER (maybe)\n')


def get_timezone(message):
    if check_info_string(message.from_user.id, FIELDNAME_TIMEZONE, message.text):
        bot.send_message(message.from_user.id, got_it_string)
        bot.send_message(message.from_user.id, give_me_time_string)
        bot.register_next_step_handler(message, get_time)
    else:
        bot.send_message(message.from_user.id, something_went_wrong_string)
        bot.register_next_step_handler(message, get_timezone)


def change_timezone(message):
    if check_info_string(message.from_user.id, FIELDNAME_TIMEZONE, message.text):
        bot.send_message(message.from_user.id, got_it_string)
    else:
        bot.send_message(message.from_user.id, something_went_wrong_string)
        bot.register_next_step_handler(message, change_timezone)


def get_time(message):
    if check_info_string(message.from_user.id, FIELDNAME_QUESTION_TIME, message.text):
        bot.send_message(message.from_user.id, got_it_string)
        bot.send_message(message.from_user.id, give_me_info_string, reply_markup=keyboard_yesno)
    else:
        bot.send_message(message.from_user.id, something_went_wrong_string)
        bot.register_next_step_handler(message, get_time)


def change_time(message):
    if check_info_string(message.from_user.id, FIELDNAME_QUESTION_TIME, message.text):
        bot.send_message(message.from_user.id, got_it_string)
    else:
        bot.send_message(message.from_user.id, something_went_wrong_string)
        bot.register_next_step_handler(message, change_time)


@bot.callback_query_handler(func=lambda call: call.data.startswith(INFO_PREFIX))
def callback_give_me_info(call):
    prefix_len = len(INFO_PREFIX)
    answer = call.data[prefix_len:]
    if answer == 'yes':
        bot.send_message(call.message.chat.id, give_me_sex_string, reply_markup=keyboard_sex)
    else:
        bot.send_message(call.message.chat.id, will_wait_string)


@bot.callback_query_handler(func=lambda call: call.data.startswith(SEX_PREFIX))
def callback_sex(call):
    prefix_len = len(SEX_PREFIX)
    sex = call.data[prefix_len:]
    write_info(call.message.chat.id, FIELDNAME_SEX, sex)
    bot.send_message(call.message.chat.id, give_me_age_string)
    bot.register_next_step_handler(call.message, get_age)


def get_age(message):
    if check_info_string(message.from_user.id, FIELDNAME_AGE, message.text):
        bot.send_message(message.from_user.id, got_it_string)
        bot.send_message(message.from_user.id, give_me_city_string)
        bot.register_next_step_handler(message, get_city)
    else:
        bot.send_message(message.from_user.id, something_went_wrong_string)
        bot.register_next_step_handler(message, get_age)


def change_age(message):
    if check_info_string(message.from_user.id, FIELDNAME_AGE, message.text):
        bot.send_message(message.from_user.id, got_it_string)
    else:
        bot.send_message(message.from_user.id, something_went_wrong_string)
        bot.register_next_step_handler(message, change_age)


def get_city(message):
    write_info(message.from_user.id, FIELDNAME_CITY, message.text)
    bot.send_message(message.from_user.id, got_it_string)
    bot.send_message(message.from_user.id, give_me_occupation_string, reply_markup=keyboard_occupations)


def change_city(message):
    write_info(message.from_user.id, FIELDNAME_CITY, message.text)
    bot.send_message(message.from_user.id, got_it_string)


@bot.callback_query_handler(func=lambda call: call.data.startswith(OCCUPATION_PREFIX))
def callback_occupation(call):
    prefix_len = len(OCCUPATION_PREFIX)
    write_info(call.message.chat.id, FIELDNAME_OCCUPATION, call.data[prefix_len:])
    bot.send_message(call.message.chat.id, thank_for_info_string)


@bot.callback_query_handler(func=lambda call: call.data.startswith(NEW_SEX_PREFIX))
def callback_new_sex(call):
    prefix_len = len(NEW_SEX_PREFIX)
    sex = call.data[prefix_len:]
    write_info(call.message.chat.id, FIELDNAME_SEX, sex)
    bot.send_message(call.message.chat.id, got_it_string)


@bot.callback_query_handler(func=lambda call: call.data.startswith(CHANGE_PREFIX))
def callback_update_info(call):
    prefix_len = len(CHANGE_PREFIX)
    type_info = call.data[prefix_len:]
    if type_info == FIELDNAME_SEX:
        bot.send_message(call.message.chat.id, give_me_sex_string, reply_markup=keyboard_change_sex)
    if type_info == FIELDNAME_AGE:
        bot.send_message(call.message.chat.id, give_me_age_string)
        bot.register_next_step_handler(call.message, change_age)
    if type_info == FIELDNAME_CITY:
        bot.send_message(call.message.chat.id, give_me_city_string)
        bot.register_next_step_handler(call.message, change_city)
    if type_info == FIELDNAME_QUESTION_TIME:
        bot.send_message(call.message.chat.id, give_me_time_string)
        bot.register_next_step_handler(call.message, change_time)
    if type_info == FIELDNAME_TIMEZONE:
        bot.send_message(call.message.chat.id, give_me_timezone_string)
        bot.register_next_step_handler(call.message, change_timezone)
    if type_info == NOTHING:
        bot.send_message(call.message.chat.id, ok_string)


@bot.callback_query_handler(func=lambda call: call.data.startswith(COLOR_PREFIX))
def callback_write_colors(call):
    prefix_len = len(COLOR_PREFIX)
    answer = call.data[prefix_len:]
    if answer == 'ВЫХОД':
        save_colors(call.message.chat.id, colors_dict[call.message.chat.id])
        update_person_status(call.message.chat.id, True)
        bot.send_message(call.message.chat.id, repeat_colors_string_from_list(colors_dict[call.message.chat.id]))
        bot.send_message(call.message.chat.id, wanna_change_colors_string)
        colors_dict[call.message.chat.id] = []
    else:
        colors_dict[call.message.chat.id].append(answer)
        if len(colors_dict[call.message.chat.id]) == MAX_COLORS_CNT:
            save_colors(call.message.chat.id, colors_dict[call.message.chat.id])
            update_person_status(call.message.chat.id, True)
            bot.send_message(call.message.chat.id, repeat_colors_string_from_list(colors_dict[call.message.chat.id]))
            bot.send_message(call.message.chat.id, wanna_change_colors_string)
            colors_dict[call.message.chat.id] = []


@bot.message_handler(commands=['write_to_all'])
def write_to_all(message):
    if message.from_user.id == my_id:
        bot.send_message(message.from_user.id, give_me_message_to_all_string)
        bot.register_next_step_handler(message, send_message_to_all)


def send_message_to_all(message):
    user_ids = get_all_ids()
    for user_id in user_ids:
        log_str(f'user_id: {user_id}   sent message from Maria\n')
        bot.send_message(user_id, message.text)
    log_str(f'Maria wrote:  {message.text}\n')


if __name__ == '__main__':
    log_str('Bot started\n')
    try:
        bot.polling(none_stop=True)
    except:
        pass



