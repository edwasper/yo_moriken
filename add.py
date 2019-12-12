from setting import select_set,users
import Tkinter as tk
class Add(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.create_widget()

    def create_widget(self):
        self.master.title("POSTURE RIGHTING")
        frame2 = tk.Frame(master=self)
        btn = tk.Button(master=frame2,
                text="Back",
                width=5,
                bg = "#00a4e4",
                fg = "#ffffff",
                command=self.master.backToStart)
        btn.pack(anchor=tk.NW)

        lbl = tk.Label(frame2, text="Please input username", height=5, font=("Migu 1M",20))
        lbl.pack()
        editBox = tk.Entry(width=100)
        editBox.pack(anchor=tk.CENTER)
        endbtn = tk.Button(master=frame2,
                text="select",
                width=10,
                bg="#00a4e4",
                fg="#ffffff",
                command=self.selectUserName(editBox.get()))
        endbtn.pack()


    def selectUserName(self,get_val):
        username.append(get_val)
        self.master.backToStart()

