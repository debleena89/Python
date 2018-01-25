#!/usr/bin/python3

from tkinter import *
fields = 'Number of States'

def fetch(entries):
   print("In the fetch")
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print("there is text",)
      for index in range(0,int(entry[1].get())):
           print("good")
           row = Frame(root)
           lab = Label(row, width=15, text="Enter state", anchor='w')
           enter_state = Entry(row)
           entries.append((fields, enter_state))
      print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
   print("In the makeform")
   entries = []
   row = Frame(root)
   lab = Label(row, width=15, text=fields, anchor='w')
   ent = Entry(row)
   print("hi",ent.get())
   row.pack(side=TOP, fill=X, padx=5, pady=5)
   lab.pack(side=LEFT)
   ent.pack(side=RIGHT, expand=YES, fill=X)
   entries.append((fields, ent))
   return entries

if __name__ == '__main__':
   print("In the mainl")
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   print("show command done")
   b1.pack(side=LEFT, padx=5, pady=5)
   print("show  pack command done")
   b2 = Button(root, text='Quit', command=root.quit)
   print("quit command done")
   b2.pack(side=LEFT, padx=5, pady=5)
   print("quit pack command done")
   root.mainloop()
   print("come to the end")
