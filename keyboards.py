from keyboa import keyboa_maker
from fieldnames import color_names

colors = [{color: 'color_' + color} for color in color_names + ['ВЫХОД']]
keyboard_colors = keyboa_maker(items=colors, copy_text_to_callback=True, items_in_row=3)

occupations = [{'Школьник': 'occupation_kid'},
               {'Студент': 'occupation_student'},
               {'Работаю': 'occupation_worker'},
               {'Пенсионер': 'occupation_retiree'},
               {'Что-то еще': 'occupation_unknown'}]
keyboard_occupations = keyboa_maker(items=occupations)

answers = [{'Ответить сейчас': 'answer_now'},
           {'Ответить позже': 'answer_later'},
           {'Игнорировать': 'answer_never'}]
keyboard_answers = keyboa_maker(items=answers)

personal_info = [{'Пол': 'change_sex'},
                 {'Возраст': 'change_age'},
                 {'Город': 'change_city'},
                 {'Время вопроса': 'change_question_time_minutes'},
                 {'Часовой пояс': 'change_timezone'},
                 {'Ничего менять не надо': 'change_nothing'}]
keyboard_change_info = keyboa_maker(items=personal_info)

info_yesno = [{'Да': 'info_yes'}, {'Нет': 'info_no'}]
keyboard_yesno = keyboa_maker(items=info_yesno)

info_sex = [{'Мужской': 'sex_male'}, {'Женский': 'sex_female'}]
keyboard_sex = keyboa_maker(items=info_sex)

change_sex = [{'Мужской': 'new_sex_male'}, {'Женский': 'new_sex_female'}]
keyboard_change_sex = keyboa_maker(items=change_sex)
