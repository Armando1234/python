import datetime
import sys
import time


while True:
    print(datetime.datetime.now())


while True:
 
    if datetime.timedelta(datetime.datetime.now(), start_time) > 1000:
        sys.exit()
    else:
        continue