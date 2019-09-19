import sys
import time
import random
import threading
from datetime import datetime


gloarg = 0

def senyi(arg,sai,flag=True):
    sai *= 100
    if not flag :
        sai = -sai
    if sai%2==0 :
        arg += sai
    else :
        arg -= sai

    return arg


def randcalc(arg):
    deme = random.randint(0,12)
    if arg<7000:
        arg = senyi(arg,deme)
    else :
        arg = senyi(arg,deme,False)
    return arg

def measure_time():
    global gloarg
    val = 0
    sit_flag = False
    sit_count = 0
    sit_ref = 7000
    head = datetime.now()
    tail = datetime.now()
    sit_time = [tail.hour-head.hour, tail.minute-head.minute, tail.second-head.second]

    try :
        while True:
            val = gloarg
            if sit_flag :
                sit_count += 1
                if val < sit_ref:
                    sit_flag = False
                    tail = datetime.now()
                    sit_time = [tail.hour-head.hour, tail.minute-head.minute, tail.second-head.second]
                    for tmp in sit_time :
                        if tmp < 0:
                            sittime[sit_time.index(tmp)] = tmp + 60
                    if sit_time[0] >48 :
                        sit_time[0] -= 48

                    print("sit_count:",sit_count)
                    print("sit_time:",sit_time)
                    sit_count = 0
            else :
                if val > sit_ref:
                    sit_flag = True
                    head = datetime.now()
            time.sleep(0.5)

    except :
        print("emergency_timer")

timer_thread = threading.Thread(target = measure_time)
timer_thread.start()

try :
    while True:
        gloarg = randcalc(gloarg)
        print(gloarg)
        time.sleep(0.5)
except :
    print("emergency_main")
