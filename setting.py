import Tkinter as tk
import ttk
from add import Add
from setuser import SetUser

username = ["guest"]
select_set = "guest"
users = {"guest":[0.5,0]}

class Setting(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)        
        self.Applist = [Add,SetUser]
	self.create_widget()

    def create_widget(self):
        global username
        self.master.title("POSTURE RIGHTING")
        frame1 = tk.Frame(master = self)
        btn = tk.Button(master=frame1,
                text="Back",
                width=5,
                bg = "#00a4e4",
                fg = "#ffffff",
                command=self.master.backToStart)
        btn.pack(anchor=tk.NW)

        lbl = tk.Label(frame1, text="Please user setting", height=5, font=("Migu 1M",20))
        lbl.pack()
        plsbtn = tk.Button(master=frame1,
                text="Add User",
                width=10,
                bg = "#00a4e4",
                fg = "#ffffff",
                command=self.changeApp(0))
        plsbtn.pack(anchor=tk.NE)

        combo = ttk.Combobox(frame1,value=username)
        combo.current(0)
        combo.pack()

        slctbtn = tk.Button(text=select,command=self.changeSetUser(combo.get())
        slctbtn.pack()

    def changeApp(self,i):
        return lambda :self.master.change(self.Applist[i])

    def changeSetUser(self,get_val):
        global select_set
        select_set = get_val
        self.changeApp(1)
        
        

