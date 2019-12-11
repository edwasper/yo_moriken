import Tkinter as tk
class DummyApp(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("No application registered.")

        btn = tk.Button(master=self,
                text="Back",
                width=5,
                bg = "#00a4e4",
                fg = "#ffffff",
                command=self.master.backToStart)
        btn.pack(anchor=tk.NW)

        lbl = tk.Label(self, text="No application registered here.", height=5, font=("Migu 1M",20))
        lbl.pack()
