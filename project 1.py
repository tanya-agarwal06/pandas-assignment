from tkinter import *

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing,accelerator="Ctrl+N" )
filemenu.add_command(label="Open", command=donothing, accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=donothing, accelerator="Ctrl+S")
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
editmenu.add_command(label="Bold", command= donothing, accelerator="Ctrl+B")
editmenu.add_command(label="Italic", command= donothing, accelerator="Ctrl+I")
editmenu.add_command(label="Underline", command= donothing, accelerator="Ctrl+U")
editmenu.add_command(label="Overstrike", command= donothing, accelerator="Ctrl+T")
editmenu.add_command(label="Undo", command=donothing, accelerator="Ctrl+Z")
editmenu.add_command(label="Redo", command=donothing, accelerator="Ctrl+Y")

root.config(menu=menubar)

root.mainloop()