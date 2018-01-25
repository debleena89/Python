import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.create_states()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def create_states(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Input states"
        self.hi_there["command"] = self.say_by
        self.hi_there.pack(side="top")

        self.states = tk.Button(self, text="Input states", fg="red")
        self.states.pack(side="bottom")

    def say_by(self):
        print("hello give text input")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
