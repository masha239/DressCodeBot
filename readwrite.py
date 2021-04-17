from pymongo import MongoClient
from datetime import datetime, timedelta

dbname = 'dresscode'
collection_name_persons = 'persons'
collection_name_colors = 'colors'
collection_name_messages = 'messages'


def get_id_and_token():
    config_filename = 'config.txt'
    with open(config_filename, 'r') as f:
        result = [line.strip() for line in f.readlines()]
        return result[0], int(result[1])


def log_str(msg: str):
    dts = datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')
    logfile_name = 'log.txt'
    with open(logfile_name, 'a') as f:
        f.write("%s    %s" % (dts, msg))


def write_info(user_id, feature_name, feature_value):
    client = MongoClient()
    collection = client[dbname][collection_name_persons]
    collection.update_one({'user_id': user_id}, {"$set": {feature_name: feature_value}}, upsert=True)
    log_str(f'user_id: {user_id}   updated {feature_name} : {feature_value}\n')
    if feature_name in ['timezone', 'question_time_minutes']:
        update_user_time(user_id)


def save_user(user_id):
    client = MongoClient()
    collection = client[dbname][collection_name_persons]
    collection.update_one({'user_id': user_id}, {'$set': {'answer_status': False}}, upsert=True)


def save_message(user_id, text):
    client = MongoClient()
    collection = client[dbname][collection_name_messages]
    collection.insert_one({'user_id': user_id, 'text': text, 'time': datetime.utcnow()})
    log_str(f'user_id: {user_id}   saved message from user\n')


def save_colors(user_id, colors):
    client = MongoClient()
    collection = client[dbname][collection_name_colors]
    collection.insert_one({'user_id': user_id, 'date': datetime.utcnow(), 'colors': colors})
    log_str(f'user_id: {user_id}   saved colors\n')


def get_occupation(english_word):
    occupations = {'kid': 'Школьник', 'student': 'Студент', 'worker': 'Работаю', 'retiree': 'Пенсионер', 'unknown': 'Что-то еще'}
    return occupations[english_word]


def get_settings(user_id):
    client = MongoClient()
    collection = client[dbname][collection_name_persons]
    try:
        doc = collection.find({'user_id': user_id}, limit=1)[0]
        settings_dict = dict()
        settings_string = ''
        for feature in doc.keys():
            value = doc[feature]
            if feature == 'timezone':
                if value > 0:
                    value = '+' + str(value)
                else:
                    value = str(value)
                settings_dict['Временная зона'] = value
            elif feature == 'question_time_minutes':
                minutes = str(value % 60)
                if len(minutes) == 1:
                    minutes = '0' + minutes
                hours = str(value // 60)
                if len(hours) == 1:
                    hours = '0' + hours
                settings_dict['Время суток'] = hours + ':' + minutes
            elif feature == 'sex':
                if value == 'male':
                    settings_dict['Пол'] = 'Мужской'
                else:
                    settings_dict['Пол'] = 'Женский'
            elif feature == 'age':
                settings_dict['Возраст'] = str(value)
            elif feature == 'city':
                settings_dict['Город'] = value
            elif feature == 'occupation':
                settings_dict['Род занятий'] = get_occupation(value)

        for feature in settings_dict.keys():
            settings_string += feature + ' ' + settings_dict[feature] + '\n'

        return settings_dict, settings_string

    except Exception as exteption:
        print(str(exteption))
        return dict(), 'Error'


def update_user_time(user_id):
    client = MongoClient()
    collection = client[dbname][collection_name_persons]
    doc_user = collection.find({'user_id': user_id})[0]
    question_time_minutes = doc_user.get('question_time_minutes', 0)
    timezone = doc_user.get('timezone', 0)
    minutes_in_day = 24 * 60
    minutes_in_hour = 60
    utc_minutes = (question_time_minutes + minutes_in_day - timezone * minutes_in_hour) % minutes_in_day
    collection.update_one({'user_id': user_id}, {'$set': {'utc_question_time_minutes': utc_minutes}})
    collection.update_one({'user_id': user_id}, {'$set': {'utc_midnight_time_minutes': (minutes_in_day - timezone * minutes_in_hour) % minutes_in_day}})
    log_str(f'user_id: {user_id}   updated user time: utc_question_time {utc_minutes}, midnight_time {(minutes_in_day - timezone * 60) % minutes_in_day}\n')


def update_person_status(user_id, status):
    client = MongoClient()
    collection = client[dbname][collection_name_persons]
    collection.update_one({'user_id': user_id}, {'$set': {'answer_status': status}})
    log_str(f'user_id: {user_id}  updated answer_status to {status}\n')


def get_ids_to_send():
    client = MongoClient()
    collection = client[dbname][collection_name_persons]
    now = datetime.utcnow()
    minute = now.hour * 60 + now.minute
    log_str(f'minute = {minute}\n')
    for doc in collection.find({'utc_midnight_time_minutes': minute}):
        update_person_status(doc['user_id'], False)
    return [doc['user_id'] for doc in collection.find({'utc_question_time_minutes': minute})]



def get_all_ids():
    client = MongoClient()
    collection = client[dbname][collection_name_persons]
    return [doc['user_id'] for doc in collection.find()]




