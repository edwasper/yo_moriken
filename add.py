import setting
import Tkinter as tk
class Add(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("POSTURE RIGHTING")

        btn = tk.Button(master=self,
                text="Back",
                width=5,
                bg = "#00a4e4",
                fg = "#ffffff",
                command=self.master.backToStart)
        btn.pack(anchor=tk.NW)

        lbl = tk.Label(self, text="Please input username", height=5, font=("Migu 1M",20))
        lbl.pack()
        editBox = tk.Entry(width=100)
        editBox.pack()
        endbtn = tk.Button(master=self,
                text="select",
                width=10,
                bg="#00a4e4",
                fg="#ffffff",
                command=self.selectUserName)
        endbtn.pack()


    def selectUserName():
        setting.username.append(editBox.get())
        self.master.backToStart()

