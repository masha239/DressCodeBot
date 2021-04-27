import telebot
from colors import make_pie_chart, sort_colors, make_hist
from readwrite import get_id_and_token, log_str, get_all_color_records_user, get_all_ids, get_last_week_plus3
from infostrings import piechart_string, get_number_answers_string, hist_string
import os
import time


token, my_id = get_id_and_token()
bot = telebot.TeleBot(token)


if __name__ == '__main__':
    user_ids = get_all_ids()
    all_colors = []

    for user_id in user_ids:
        try:
            time_start, time_finish = get_last_week_plus3(user_id)
            all_records_user, timezone_user = get_all_color_records_user(user_id, time_start, time_finish)

            if len(all_records_user) > 0:
                colors_user = sort_colors(timezone_user, all_records_user)
                all_colors += colors_user
                filename = make_pie_chart(user_id, colors_user)
                bot.send_message(user_id, piechart_string)
                bot.send_photo(user_id, open(filename, 'rb'))
                bot.send_message(user_id, get_number_answers_string(len(colors_user)))
                log_str(f'user_id: {user_id}   sent piechart\n')
                os.remove(filename)
            time.sleep(1)
        except Exception as e:
            log_str(str(e) + '\n')

    filename_hist = make_hist(all_colors)
    for user_id in user_ids:
        try:
            bot.send_message(user_id, hist_string)
            bot.send_photo(user_id, open(filename_hist, 'rb'))
            log_str(f'user_id: {user_id}   sent piechart\n')
            time.sleep(1)
        except Exception as e:
            log_str(str(e) + '\n')
