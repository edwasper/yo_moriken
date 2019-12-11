import Tkinter as tk
from dummy import DummyApp
from add import Add
from setting import Setting
from setuser import SetUser


class FrameBase(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x600")
        self.frame = StartPageFrame(self)
        self.frame.pack(expand=True, fill="both")
        #self.attributes("-fullscreen", True)

    def change(self, frame):
        self.frame.pack_forget() # delete currrent frame
        self.frame = frame(self)
        self.frame.pack(expand=True, fill="both") # make new frame


    def changeAddUser(self):
        self.frame.pack_foget()
        self.frame = Add(self)
        self.frame.pack(expand=True, fill="both")


    def changeSetUser(self,name):
        self.frame.pack_foget()
        self.frame = SetUser(self,user=name)
        self.frame.pack(expand=True, fill="both")


    def backToStart(self):
        self.frame.pack_forget()
        self.frame = StartPageFrame(self)
        self.frame.pack(expand=True, fill="both")

class StartPageFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("POSTURE RIGHTING")

        self.grid(column=0, row=0, sticky=tk.NSEW)

        self.Applist = [
                    [ [Setting, "Setting"], [DummyApp, "Not Registerd"] ], 
                    [ [DummyApp, "Not Registerd"], [DummyApp, "Not Registerd"] ]
                    ]

        lbl = tk.Label(master=self, text ="main menu", font=("Migu 1M",20))
        lbl.grid(column=0,row=0,sticky=tk.NW, padx=10)
        #btn = tk.Button(
        #   master = self,
        #   text="Close",
        #    width = 5,
        #    bg = "#dc143c",
        #    fg = "#ffffff",
        #    command=self.master.destroy)
        #btn.grid(column=2, row=0,sticky=tk.NE)

        for r in range(1,3):
            for c in range(2):
                btn = tk.Button(
                        master=self,
                        wraplength=5,
                        justify=tk.LEFT,
                        text=self.Applist[r-1][c][1],
                        font=("Migu 1M", 16),
                        width=100,
                        bg="#e6e6fa",
                        command=self.gotoApp(r-1,c))
                btn.grid(column=c, row=r, padx=10, pady=10, sticky=tk.NSEW)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def gotoApp(self,r,c):
        return lambda :self.master.change(self.Applist[r][c][0])

if __name__=="__main__":
    app=FrameBase()
    app.mainloop()

