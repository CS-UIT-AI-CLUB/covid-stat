import schedule
import time
from utils import fetch_data

def job():
    data = fetch_data()
    t = int(time.time())
    print('Done fetching data. Timestamp = {}'.format(t))
    
    
if __name__ == '__main__':
    # Fetch data every 10 minutes
    schedule.every(10).minutes.do(job)
    while True:
        schedule.run_pending()