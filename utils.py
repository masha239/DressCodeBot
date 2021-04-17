from readwrite import write_info


def check_info_string(user_id, info_type, info_string):
    if info_type == 'age':
        try:
            age = int(info_string)
            if 0 < age < 100:
                write_info(user_id, info_type, age)
                return True
            else:
                return False
        except:
            return False

    if info_type == 'timezone':
        try:
            timezone = int(info_string)
            if abs(timezone) <= 12:
                write_info(user_id, info_type, timezone)
                return True
            else:
                return False
        except:
            return False

    if info_type == 'question_time_minutes':
        min_hours = 0
        min_minutes = 0
        max_hours = 23
        max_minutes = 59
        minutes_in_hour = 60
        try:
            hours, minutes = [int(number) for number in info_string.split(':')]
            if hours >= min_hours and hours <= max_hours and minutes >= min_minutes and minutes <= max_minutes:
                question_time_minutes = minutes_in_hour * hours + minutes
                write_info(user_id, info_type, question_time_minutes)
                return True
            else:
                raise Exception('Wrong time')
        except:
            return False
