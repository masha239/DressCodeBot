
from pymongo import MongoClient
from readwrite import update_user_time
from datetime import datetime, timedelta

db = MongoClient()['dresscode']
persons = db['persons']
messages = db['messages']
colors = db['colors']



for doc in persons.find():
    for field in doc.keys():
        print(field, doc[field])
    #for doc1 in colors.find({'user_id': doc['user_id']}):
    #    print(doc1['date'], doc1['colors'])
    print()

for doc in messages.find({'time': {'$gte': datetime.now() - timedelta(hours=96)}}):
    print(doc['user_id'], doc['time'], doc['text'])
