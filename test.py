from pymongo import MongoClient
from readwrite import update_user_time
from datetime import datetime, timedelta

db = MongoClient()['dresscode']
persons = db['persons']
messages = db['messages']
colors = db['colors']



for doc in persons.find():
    for field in doc.keys():
        if field not in ['sex', 'age', '_id', 'occupation', 'city']:
           print(field, doc[field])
    print()

for doc in messages.find({'time': {'$gte': datetime.now() - timedelta(hours=96)}}):
    print(doc['user_id'], doc['time'], doc['text'])
