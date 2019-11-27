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
keisu = 600
plot_count = 0

##set_nomal##
try:
    foge = raw_input("set_nomal")
    print(foge)
    f_nomal = []
    b_nomal = []
    while plot_count<keisu :
        f_arg = abs(f_hx.get_weight(5))
        b_arg = abs(b_hx.get_weight(5))
        f_nomal.append(f_arg)
        b_nomal.append(b_arg)

        print("front_roadcell:",f_nomal[plot_count])
        print("back_roadcell:",b_nomal[plot_count])

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
    if len(f_nomal) == len(b_nomal):
	set_count(f_nomal)
    elif len(f_nomal) > len(b_nomal):
	while(len(f_nomal) > len(b_nomal)):
	    del f_nomal[len(f_nomal)-1] 
	set_count(f_nomal)
    elif len(f_nomal) < len(b_nomal):
	while(len(f_nomal) < len(b_nomal)):
	    del b_nomal[len(b_nomal)-1]
	set_count(f_nomal)
    

    inp = raw_input("please input file name\n")
    with open(inp + ".csv",'wt') as f:
        for i in range(keisu):
	    f.write(f_nomal[i])
            f.write(',')
            f.write(b_nomal[i])
            f.write('\n')



    plt.plot(range(plot_count),b_nomal)
    plt.plot(range(plot_count),f_nomal)
    plt.title('Pressure applied during measurement') 
    plt.xlabel('over time')
    plt.ylabel('pressure')
    plt.ylim(0,30000)
    plt.show()

    #cleanAndExit()


##set_slouch##

plot_count = 0
try:
    foge = raw_input("set_slouch")
    print(foge)
    f_slouch = []
    b_slouch = []
    while plot_count<keisu :
        f_arg = abs(f_hx.get_weight(5))
        b_arg = abs(b_hx.get_weight(5))
        f_slouch.append(f_arg)
        b_slouch.append(b_arg)
        print("front_roadcell:",f_slouch[plot_count])
        print("back_roadcell:",b_slouch[plot_count])

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
    if len(f_slouch) == len(b_slouch)):
	set_count(f_slouch)
    elif len(f_slouch) > len(b_slouch):
	while(len(f_slouch) > len(b_slouch)):
	    del f_slouch[len(f_slouch)-1] 
	set_count(f_slouch)
    elif len(f_slouch) < len(b_slouch):
	while(len(f_nomal) < len(b_slouch)):
	    del b_slouch[len(b_slouch)-1]
	set_count(f_slouch)
    

    inp = raw_input("please input file name\n")
    with open(inp + ".csv",'wt') as f:
        for i in range(keisu):
	    f.write(f_slouch[i])
            f.write(',')
            f.write(b_slouch[i])
            f.write('\n')



    plt.plot(range(plot_count),b_slouch)
    plt.plot(range(plot_count),f_slouch)
    plt.title('Pressure applied during measurement') 
    plt.xlabel('over time')
    plt.ylabel('pressure')
    plt.ylim(0,30000)
    plt.show()

    #cleanAndExit()



##set_warp##

plot_count = 0
try:
    foge = raw_input("set_warp")
    print(foge)
    f_warp = []
    b_warp = []
    while plot_count<keisu :
        f_arg = abs(f_hx.get_weight(5))
        b_arg = abs(b_hx.get_weight(5))
        f_warp.append(f_arg)
        b_warp.append(b_arg)
        print("front_roadcell:",f_warp[plot_count])
        print("back_roadcell:",b_warp[plot_count])

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
    if len(f_warp) == len(b_warp)):
	set_count(f_warp)
    elif len(f_warp) > len(b_warp):
	while(len(f_warp) > len(b_warp)):
	    del f_warp[len(f_warp)-1] 
	set_count(f_warp)
    elif len(f_warp) < len(b_warp):
	while(len(f_warp) < len(b_warp)):
	    del b_warp[len(b_warp)-1]
	set_count(f_warp)
    

    inp = raw_input("please input file name\n")
    with open(inp + ".csv",'wt') as f:
        for i in range(keisu):
	    f.write(f_warp[i])
            f.write(',')
            f.write(b_warp[i])
            f.write('\n')



    plt.plot(range(plot_count),b_warp)
    plt.plot(range(plot_count),f_warp)
    plt.title('Pressure applied during measurement') 
    plt.xlabel('over time')
    plt.ylabel('pressure')
    plt.ylim(0,30000)
    plt.show()

    #cleanAndExit()



