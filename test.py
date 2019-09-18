import sys
import time
import random
from datetime import datetime


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
    val = 0
    sit_flag = False
    sit_count = 0

    head = datetime.now()
    tail = datetime.now()
    sit_time = [tail.hour-head.hour, tail.minute-head.minute, tail.second-head.second]

    try :
        while True:
            val = randcalc(val)
            if sit_flag :
                sit_count += 1
                if val < 7000:
                    sit_flag = False
                    tail = datetime.now()
                    sit_time = [tail.hour-head.hour, tail.minute-head.minute, tail.second-head.second]
                  
                    print("sit_count:",sit_count)
                    print("sit_time:",sit_time)
                    sit_count = 0
            else :
                if val > 7000:
                    sit_flag = True
                    head = datetime.now()
            print(val)
            time.sleep(0.5)

    except :
        print("emergency")


measure_time()
