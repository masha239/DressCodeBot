from matplotlib import pyplot as plt
from datetime import datetime
from os import path


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
        'коричневый': 'saddlebrown',
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


def make_hist(colors_list):
    all_colors = []
    for record in colors_list:
        all_colors += record['colors']
    unique_colors = list(set(all_colors))
    unique_colors.sort(key=lambda color: all_colors.count(color))
    colors_cnt = [all_colors.count(color) for color in unique_colors]
    python_colors = [get_color_name(color) for color in unique_colors]

    fig, ax = plt.subplots()

    ax.barh(unique_colors, colors_cnt, color=python_colors)

    fig.set_figwidth(20)
    fig.set_figheight(20)
    fig.set_facecolor('white')
    ax.set_facecolor('gainsboro')
    ax.set_yticklabels(unique_colors,
                       fontsize = 20,
                       color = 'black')
    filename = f'{datetime.now().timestamp()}.png'
    full_name = path.join('hists', filename)
    plt.savefig(full_name)
    plt.close()
    return full_name
