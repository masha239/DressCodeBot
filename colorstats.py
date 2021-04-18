import telebot
from colors import make_pie_chart, sort_colors
from readwrite import get_id_and_token, log_str, get_all_color_records_user, get_all_ids, get_last_week
from infostrings import piechart_string
import os


token, my_id = get_id_and_token()
bot = telebot.TeleBot(token)


if __name__ == '__main__':
    user_ids = get_all_ids()

    for user_id in user_ids:
        try:
            time_start, time_finish = get_last_week(user_id)
            all_records_user, timezone_user = get_all_color_records_user(user_id, time_start, time_finish)
            colors_user = sort_colors(timezone_user, all_records_user)
            filename = make_pie_chart(user_id, colors_user)
            bot.send_message(my_id, piechart_string)
            bot.send_photo(my_id, open(filename, 'rb'))
            log_str(f'user_id: {user_id}   sent piechart\n')
            os.remove(filename)
        except Exception as e:
            log_str(str(e) + '\n')
