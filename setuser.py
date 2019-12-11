import Tkinter as tk
import tkMessageBox
import setting as Seting
import math
import numpy as np
import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711




class SetUser(tk.Frame):
    def __init__(self,user, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("POSTURE RIGHTING")

        #lbl = tk.Label(self, text="Please posture righting", height=5, font=("Migu 1M",20))
        #lbl.pack()

        f_referenceUnit = 2.9
	b_referenceUnit = 1
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
 
	keisu = 600 
        posture = ["normal","slouch","warp"] 
        wari=[]

        for i in range(len(posture)):
	    try:
                pop = tkMessageBox.showinfo("POSTURE RIGHTING","Please posture "+posture[i])
                lbl = tk.Label(self, text="Please posture "+posture[i], height=5, font=("Migu 1M",20))
                lbl.pack()
       
		plot_count = 0 
		f_list = []
		b_list = []
		while plot_count<keisu :
		    f_arg = abs(f_hx.get_weight(1))
		    b_arg = abs(b_hx.get_weight(1))
		    f_list.append(f_arg)
		    b_list.append(b_arg)

		    print("front_roadcell:",f_list[plot_count])
		    print("back_roadcell:",b_list[plot_count])
		    plot_count += 1

		    f_hx.power_down()
		    b_hx.power_down()
		    f_hx.power_up()
		    b_hx.power_up()
	    except :
		pass
	    finally :
		f_ave = np.mean(f_list)
		b_ave = np.mean(b_list)
		if b_ave>f_ave:
		    wari.append((b_ave-f_ave)/b_ave)
                elif b_ave<f_ave:
                    wari.append(-1*(f_ave-b_ave)/f_ave)
                else:
                    wari.append(0)

                lbl.pack_foget()
        Setting.users[user] = wari
	cleanAndExit()
        self.master.backToStart()



		
