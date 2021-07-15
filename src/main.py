import schedule
import time
import os
from pymongo import MongoClient

from utils import fetch_data

mongo_uri = 'mongodb://' + \
                os.environ['MONGO_INITDB_ROOT_USERNAME'] + ':' + \
                os.environ['MONGO_INITDB_ROOT_PASSWORD'] + '@' + \
                'mongo:27017'

client = MongoClient(mongo_uri)
db = client.covidstat

def job():
    data = fetch_data()
    t = int(time.time())
    data['timestamp'] = t
    print('Done fetching data. Timestamp = {}'.format(t))
    db.data.insert_one(data)
    print('Done inserting into database.')
    
if __name__ == '__main__':
    print('Start worker')
    job()
    # Fetch data every 10 minutes
    schedule.every(10).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)