
import time
from traceback import print_tb


def countdown(t):       #t is number of secs
    while t:
        mins,secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer,end='\r')
        time.sleep(1)
        t -= 1

    print('Timer completed')

t= input('Enter time in second:')

countdown(int(t))
    