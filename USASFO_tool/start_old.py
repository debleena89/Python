from tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    labelText=StringVar()
    labelText.set("Enter state:")
    labelDir=Label(root, textvariable=labelText, height=4)
    labelDir.pack(side="left")

    directory=StringVar(None)
    dirname=Entry(root,textvariable=directory,width=5)
    dirname.pack(side="left")

    labelText=StringVar()
    labelText.set("Enter Initial state:")
    labelDir=Label(root, textvariable=labelText, height=4)
    labelDir.pack(side="left")

    directory=StringVar(None)
    dirname=Entry(root,textvariable=directory,width=5)
    dirname.pack(side="left")

    labelText=StringVar()
    labelText.set("Enter Final state:")
    labelDir=Label(root, textvariable=labelText, height=4)
    labelDir.pack(side="left")

    directory=StringVar(None)
    dirname=Entry(root,textvariable=directory,width=5)
    dirname.pack(side="left")

    labelText=StringVar()
    labelText.set("Enter alphabets:")
    labelDir=Label(root, textvariable=labelText, height=4)
    labelDir.pack(side="left")

    directory=StringVar(None)
    dirname=Entry(root,textvariable=directory,width=5)
    dirname.pack(side="left")

    self.check_schedulability = Button(frame, 
                         text="Check Schedulability", fg="blue",
                         command=quit)
    self.check_schedulability.pack(side=LEFT)


    self.cycle_image = Button(frame,
                         text="show cycle image",
                         command=self.write_slogan)
    self.cycle_image.pack(side=LEFT)



  def write_slogan(self):
    print("Tkinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()

