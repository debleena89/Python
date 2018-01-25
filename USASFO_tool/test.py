from tkinter import Tk, Entry, StringVar, Radiobutton, W
root = Tk()

#frame = Tk.Frame(root) #"frame" represents the parent window, where the entry widget should be placed.

#frame.pack()
#GUI widgets
entry = Entry(root, width=80) #The syntax of an entry widget 

entry.pack(side='right')

#callbacks
def enableEntry():
    entry.configure(state="normal")
    entry.update()

def disableEntry():
    entry.configure(state="disabled")
    entry.update()



#def click(key):
    #print the key that was pressed
    #print key.char    


var = StringVar()
disableEnButton = Radiobutton(root, text="Disable", variable=var, value="0", command=disableEntry)
disableEnButton.pack(anchor=W)
enableEnButton = Radiobutton(root, text="Enable", variable=var, value="1", command=enableEntry)
enableEnButton.pack(anchor=W)

root.mainloop()
