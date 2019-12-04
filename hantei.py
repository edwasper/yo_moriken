#! /usr/bin/python2
import matplotlib.pyplot as plt
import math
import numpy as np
import time
import sys

EMULATE_HX711=False

f_referenceUnit = 2.9
b_referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()


def set_count(plot_list):
    global plot_count
    l_len = len(plot_list)
    if l_len != plot_count:
        if l_len > plot_count:
            while(l_len != plot_count):
                plot_count += 1
        else:
            while(l_len != plot_count):
                plot_count -= 1


f_hx = HX711(5, 6)
b_hx = HX711(23,24)
f_hx.set_reading_format("MSB", "MSB")
b_hx.set_reading_format("MSB", "MSB")

f_hx.set_reference_unit(f_referenceUnit)
b_hx.set_reference_unit(b_referenceUnit)

f_hx.reset()
b_hx.reset()

f_hx.tare()
b_hx.tare()

print("Tare done! Add weight now...")

f_plot_list = []
b_plot_list = []
f_arg = 0
b_arg = 0

wari = 0
wari_list = []
plot_count = 0
bad_list = []

count_max = 600
bad_max = 100

WARP = 2
warp_thres = 0
SLOUCH = 1
slouch_thres = 0.5
try:
    while plot_count < count_max :
        f_arg = abs(f_hx.get_weight(1))
        b_arg = abs(b_hx.get_weight(1))
        f_plot_list.append(f_arg)
        b_plot_list.append(b_arg)
        wari = (b_arg-f_arg)/b_arg
        wari_list.append(wari)

        print("front_roadcell:",f_arg)
        print("back_roadcell:",b_arg)
        print("wari:",wari)

        if (wari<warp_thres):
            print("warp posture!")
            bad_list.append(WARP)
        elif  (wari<slouch_thres):
            print("slouch posture!")
            bad_list.append(SLOUCH)
        else:
            bad_list.append(0)

        plot_count += 1
        print(plot_count)

        f_hx.power_down()
        b_hx.power_down()
        f_hx.power_up()
        b_hx.power_up()
except :
    pass
finally :
    if len(f_plot_list) == len(b_plot_list):
	set_count(f_plot_list)
    elif len(f_plot_list) > len(b_plot_list):
	while(len(f_plot_list) > len(b_plot_list)):
	    del f_plot_list[len(f_plot_list)-1] 
	set_count(f_plot_list)
    elif len(f_plot_list) < len(b_plot_list):
	while(len(f_plot_list) < len(b_plot_list)):
	    del b_plot_list[len(b_plot_list)-1]
	set_count(f_plot_list)
    

    inp = raw_input("please input file name\n")
    with open(inp + ".csv",'wt') as f:
	for i in range(plot_count):
            f.write(str(f_plot_list[i]))
            f.write(',')
            f.write(str(b_plot_list[i]))
            f.write(',')
            f.write(str(bad_list[i]))
            f.write(',')
            f.write(str(wari_list[i]))
            f.write('\n')


    plt.plot(range(plot_count),b_plot_list)
    plt.plot(range(plot_count),f_plot_list)
    plt.title('Pressure applied during measurement') 
    plt.xlabel('over time')
    plt.ylabel('pressure')
    plt.show()

    cleanAndExit()


