
from pymongo import MongoClient
from readwrite import update_user_time
from datetime import datetime, timedelta

db = MongoClient()['dresscode']
persons = db['persons']
messages = db['messages']
colors = db['colors']

print(persons.count_documents({}))
print(persons.count_documents({'answer_status': True}))
print(colors.count_documents({}))

