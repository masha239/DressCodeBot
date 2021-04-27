help_string = '''
/start - начать все с начала
/settings - посмотреть свои данные (можно что-то поменять)
/help - вот это информационное сообщение
/write - написать сообщение разработчику
/send_colors - ответить на вопрос про цвета прямо сейчас!
'''

welcome_string = '''
Привет! Я - DressCodeBot и меня очень интересуют цвета одежды.
Правда ли, что летом люди выбирают более светлую одежду?
Что женщины одеваются ярче мужчин?
Что "цвета сезона" действитеьно чаще носят в этом сезоне?
Чтобы узнать об этом, каждый день я буду спрашивать тебя о цветах твоей одежды.
Ты сможешь выбрать до 4 основных цветов.
По результатам я буду подводить статистику и иногда что-то тебе писать :)
'''

give_me_timezone_string = '''
Пожалуйста, укажи свой часовой пояс в формате +-N (например, для Москвы это будет +3)
'''

give_me_time_string = '''
В какое время тебе было бы удобно отвечать на вопрос об одежде? Введи, пожалуйста, ответ в формате чч:мм
'''

something_went_wrong_string = 'Что-то пошло не так, попробуй еще раз'

give_me_info_string = '''
Для подведения общей статистики по всем пользователям мне очень пригодятся дополнительные данные.
Если ты готов указать немного персональных данных (пол, возраст, город, чем занимаешься), было бы очень здорово :)
Поехали? Ответь "да" или "нет" в любом регистре
'''

will_wait_string = 'Ладно, я подожду :)'

give_me_sex_string = 'Назови, пожалуйста, свой пол'

give_me_age_string = 'Назови, пожалуйста, свой возраст (число)'

give_me_city_string = 'Напиши город, в котором ты живешь'

give_me_occupation_string = 'Чем ты занимаешься?'

thank_for_info_string = 'Спасибо! Я все записал и в назначенное время спрошу тебя про одежду :)'

got_it_string = 'Записал!'

ok_string = 'Хорошо.'

colors_question_string = 'Одежду каких цветов ты носил(а) сегодня? Укажи до четырех основных цветов или нажми ВЫХОД, выбрав меньшее количество'

give_me_question_string = 'Напиши свой вопрос'

question_is_delivered_string = 'Отправлено!'

wanna_change_string = 'Нужно ли что-то изменить?'

wanna_change_colors_string = 'Если хочешь изменить цвета, нажми /send_colors и ответь заново'

give_me_message_to_all_string = 'Что ты хочешь отправить всем?'

piechart_string = 'Так выглядит круговая диаграмма твоих цветов за прошедшую неделю!'

hist_string = 'A это распределение цветов за прошедшую неделю от всех пользователей:'

no_messages_string = 'Новых сообщений от пользователей нет'


def repeat_colors_string_from_list(colors):
    return 'Записал! Твои цвета сегодня: ' + ', '.join(colors)

def get_number_answers_string(number):
    return f'Количество дней, когда были сохранены цвета: {number}'
