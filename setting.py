import Tkinter as tk

username = []
users = {}

class Setting(tk.Frame):
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

        lbl = tk.Label(self, text="Please user setting", height=5, font=("Migu 1M",20))
        lbl.pack()
        plsbtn = tk.Button(master=self,
                text="Add User",
                width=10,
                bg = "#00a4e4",
                fg = "#ffffff",
                command=self.master.changeAddUser)
        plsbtn.pack(anchor=tk.NE)
        if not username:
            for i in range(len(username)):
                btn = tk.Button(
                        master=self,
                        wraplength=150,
                        justify=tk.LEFT,
                        text=username[i],
                        font=("Migu 1M", 16),
                        width=50,
                        bg="#e6e6fa",
                        command=self.master.changeSetUser(username[i]))
                btn.grid(column=i, row=0, pady=5)


