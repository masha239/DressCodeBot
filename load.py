# -*- coding: utf-8 -*-

import os
import pandas as pd
from readwrite import get_all_persons, get_all_colors
from fieldnames import *
from colors import get_color_name
from datetime import datetime

persons = get_all_persons()
records = get_all_colors()

persons_dict = {person[FIELDNAME_USER_ID]: person for person in persons}

df = pd.DataFrame()
df[FIELDNAME_USER_ID] = [record[FIELDNAME_USER_ID] for record in records]
df[FIELDNAME_DATE] = [record[FIELDNAME_DATE] for record in records]
df[FIELDNAME_SEX] = [persons_dict[record[FIELDNAME_USER_ID]].get(FIELDNAME_SEX, None) for record in records]
df[FIELDNAME_TIMEZONE] = [persons_dict[record[FIELDNAME_USER_ID]].get(FIELDNAME_TIMEZONE, None) for record in records]
df[FIELDNAME_AGE] = [persons_dict[record[FIELDNAME_USER_ID]].get(FIELDNAME_AGE, None) for record in records]
df[FIELDNAME_CITY] = [persons_dict[record[FIELDNAME_USER_ID]].get(FIELDNAME_CITY, None) for record in records]
df[FIELDNAME_OCCUPATION] = [persons_dict[record[FIELDNAME_USER_ID]].get(FIELDNAME_OCCUPATION, None) for record in records]
df[FIELDNAME_QUESTION_TIME] = [persons_dict[record[FIELDNAME_USER_ID]].get(FIELDNAME_QUESTION_TIME, None) for record in records]
for color in color_names:
    df[get_color_name(color)] = [1 if color in record[FIELDNAME_COLORS] else 0 for record in records]

df.to_csv(os.path.join('results', f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"))