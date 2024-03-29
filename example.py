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
# I've found out that, for some reason, the order of the bytes is not always the same between versions of python, numpy and the hx711 itself.
# Still need to figure out why does it change.
# If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
# There is some code below to debug and log the order of the bits and the bytes.
# The first parameter is the order in which the bytes are used to build the "long" value.
# The second paramter is the order of the bits inside each byte.
# According to the HX711 Datasheet, the second parameter is MSB so you shouldn't need to modify it.
f_hx.set_reading_format("MSB", "MSB")
b_hx.set_reading_format("MSB", "MSB")

# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
#hx.set_reference_unit(113)
f_hx.set_reference_unit(f_referenceUnit)
b_hx.set_reference_unit(b_referenceUnit)

f_hx.reset()
b_hx.reset()

f_hx.tare()
b_hx.tare()

print("Tare done! Add weight now...")

# to use both channels, you'll need to tare them both
#hx.tare_A()
#hx.tare_B()

f_plot_list = []
b_plot_list = []
plot_count = 0

try:
    while plot_count<600 :
        f_plot_list.append(abs(f_hx.get_weight(5)))
        b_plot_list.append(abs(b_hx.get_weight(5)))

        print("front_roadcell:",f_plot_list[plot_count])
        print("back_roadcell:",b_plot_list[plot_count])

        plot_count += 1

        # To get weight from both channels (if you have load cells hooked up 
        # to both channel A and B), do something like this
        #val_A = hx.get_weight_A(5)
        #val_B = hx.get_weight_B(5)
        #print "A: %s  B: %s" % ( val_A, val_B )

        f_hx.power_down()
        b_hx.power_down()
        f_hx.power_up()
        b_hx.power_up()
        time.sleep(0.1)
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
    f_csv = '\n'.join(f_plot_list)
    b_csv = '\n'.join(b_plot_list)
    with open(inp + "_f.csv",'wt') as f:
	f.write(f_csv)

    with open(inp + "_b.csv",'wt') as f:
	f.write(b_csv)


    plt.plot(range(plot_count),b_plot_list)
    plt.plot(range(plot_count),f_plot_list)
    plt.title('Pressure applied during measurement') 
    plt.xlabel('over time')
    plt.ylabel('pressure')
    plt.ylim(0,30000)
    plt.show()

    cleanAndExit()


