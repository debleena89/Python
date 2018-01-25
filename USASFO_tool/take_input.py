from tkinter import *



def show_entry_fields():
   for index in range(0,int(e1.get())):
       resetall.configure(state = NORMAL)
       Label(master, text="Enter states").grid(row=1)
       e2 = Entry(master)
       e2.grid(row=1, column=1)
       resetall.configure(state = DISABLED)
       print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="Enter number of states").grid(row=0)
Label(master, text="Enter states").grid(row=1)

e1 = Entry(master)


e1.grid(row=0, column=1)


resetall = Button(text = "NeXT", command = show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

#resetall.pack(side = "left")

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
#Button(master, text='Next', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
