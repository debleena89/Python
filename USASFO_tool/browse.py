#!/usr/bin/env python     
import os 
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.quit_program()
        self.browse_file()
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('musicfiles', '.mp3'),('vediofiles', '.mp4'),("All files", "*.*")]

        options['parent'] = self
        options['title'] = 'This is a title'

    def quit_program(self):
        self.quitButton = tk.Button(self, text='Quit',
          command=self.quit)            
        self.quitButton.grid()

    def browse_file(self):
        self.browseButton = tk.Button(self, text='Browse',command=self.askopenfile)
        self.browseButton.grid()
    def askopenfile(self):
        filename = filedialog.askopenfile(**self.file_opt )
        print(os.path.split(filename.name)[1])

app = Application()                       
app.master.title('Sample application')    
app.mainloop() 


