from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from os import path
from fieldnames import FIELDNAME_DATE


def get_day(date: datetime, timezone):
    corrected_date = date + timedelta(hours=timezone)
    return corrected_date.date()


def sort_colors(timezone, all_records_user):
    all_records_user.sort(key=lambda x: x[FIELDNAME_DATE])
    filtered_records = []
    for i in range(len(all_records_user) - 1):
        curr_date = get_day(all_records_user[i][FIELDNAME_DATE], timezone)
        next_date = get_day(all_records_user[i + 1][FIELDNAME_DATE], timezone)
        if curr_date != next_date:
            filtered_records.append(all_records_user[i])

    filtered_records.append(all_records_user[-1])
    return filtered_records


def get_color_name(color):
    colors_dict = {
        'белый': 'white',
        'серый': 'gray',
        'черный': 'black',
        'красный': 'red',
        'синий': 'blue',
        'желтый': 'yellow',
        'зеленый': 'green',
        'оранжевый': 'orange',
        'фиолетовый': 'purple',
        'розовый': 'pink',
        'голубой': 'lightskyblue',
        'бежевый': 'beige',
        'коричневый': 'brown',
        'сиреневый': 'orchid',
        'бордовый': 'maroon',
        'бирюзовый': 'mediumturquoise',
        'коралловый': 'coral',
        'салатовый': 'greenyellow'
    }
    return colors_dict[color]


def make_pie_chart(user_id, colors_list):
    all_colors = []
    for record in colors_list:
        all_colors += record['colors']
    unique_colors = list(set(all_colors))
    colors_cnt = [all_colors.count(color) for color in unique_colors]
    python_colors = [get_color_name(color) for color in unique_colors]
    explode = [0.1] * len(colors_cnt)
    plt.pie(colors_cnt, colors=python_colors, autopct='%1.1f%%', shadow=True, startangle=90, explode=explode)
    filename = f'{user_id}.{datetime.now().timestamp()}.png'
    full_name = path.join('piecharts', filename)
    plt.savefig(full_name)
    plt.close()
    return full_name