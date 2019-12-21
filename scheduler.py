# use this to debug the scheduler in tweety.py

import time
import schedule

def job():
    print(f'\njob started\n')

schedule.every(20).seconds.do(job)

while 1:
    t = time.ctime()
    schedule.run_pending()
    time.sleep(10)
    print(f'sleep Start {t}') 
