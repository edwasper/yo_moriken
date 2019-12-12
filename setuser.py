import Tkinter as tk
import tkMessageBox
import math
import numpy as np
import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711




class SetUser(tk.Frame):
    def __init__(self,user, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master.title("POSTURE RIGHTING")

        #lbl = tk.Label(self, text="Please posture righting", height=5, font=("Migu 1M",20))
        #lbl.pack()

        self.refUnit = [2.9,1]
	self.f_hx = HX711(5, 6)
	self.f_hx.set_reading_format("MSB", "MSB")
        self.b_hx = HX711(23,24)
	self.b_hx.set_reading_format("MSB", "MSB")
 
	self.f_hx.set_reference_unit(self.refUnit[0]) 
	self.b_hx.set_reference_unit(self.refUnit[1]) 
 
	self.f_hx.reset() 
	self.b_hx.reset() 
 
	self.f_hx.tare() 
	self.b_hx.tare() 

        self.posture = ["slouch","warp"] 
	self.keisu = 100 
        
        self.create_widget()

    def create_widget(self):
        btn = tk.Button(master=self,
                text="Back",
                width=5,
                bg = "#00a4e4",
                fg = "#ffffff",
                command=self.master.backToStart)
        btn.pack(anchor=tk.NW)

        lbl = tk.Label(master=self, text="Please select posture", height=5, font=("Migu 1M",20))
        lbl.pack()

        Sbtn = tk.Button(master=self,
                width=5,
                bg = "#00a4e4",
                text="Slouch",
                fg = "#ffffff",
                command=self.setPosturelam(0))
        Sbtn.pack()

        Wbtn = tk.Button(master=self,
                text="Warp",
                width=5,
                bg = "#00a4e4",
                fg = "#ffffff",
                command=self.setPosturelam(1))
        Wbtn.pack()
    def setPosturelam(self,pos):
        return lambda :self.setPosture(pos)

    def setPosture(self,pos):
	lbl = tk.Label(self, text="Please posture "+self.posture[pos], height=5, font=("Migu 1M",20))
	lbl.pack()

	plot_count = 0 
	f_list = []
	b_list = []

	try:
	    while plot_count<self.keisu :
		f_arg = abs(self.f_hx.get_weight(1))
		b_arg = abs(self.b_hx.get_weight(1))
		f_list.append(f_arg)
		b_list.append(b_arg)

		print("front_roadcell:",f_list[plot_count])
		print("back_roadcell:",b_list[plot_count])
		plot_count += 1
		print(plot_count)
		self.f_hx.power_down()
		self.b_hx.power_down()
		self.f_hx.power_up()
		self.b_hx.power_up()
	except :
	    pass
	finally :
	    f_ave = np.mean(f_list)
	    b_ave = np.mean(b_list)
	    if b_ave>f_ave:
		wari = ((b_ave-f_ave)/b_ave)
	    elif b_ave<f_ave:
		wari = (-1*(f_ave-b_ave)/f_ave)
	    else:
		wari = 0

	    lbl.pack_forget()
	    self.master.users[self.master.select][pos] = wari
	    GPIO.cleanup()
	    self.master.backToStart()


		    
