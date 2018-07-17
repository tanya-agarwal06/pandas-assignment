from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import simpledialog
import time
import os
from tkinter.colorchooser import askcolor
from tkinter import PhotoImage
#===============================================functions=================================================================

filename=None

def new_file(event=None):
    global filename
    filename="Untitled"
    text.delete(0.0,END)

def savefile(event=None):
    global filename
    t=text.get(0.0,END)
    f=open(filename,mode='w')
    f.write(t)
    f.close()

def saveAs():
    f=asksaveasfile(mode='w', defaultextension='.txt')
    t=text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title='oops',message='unable to save file')

def openfile(event=None):
    f=askopenfile(mode='r')
    t=f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

def exit():
    if messagebox.askyesno("Quit","Are you sure you want to quit"):
        master.destroy()


def About():
    label=messagebox.showinfo("about"," A python alternative to notepad")

def findin(event=None):
    findString =simpledialog.askstring('Find','Enter text')
    t = text.get(0.0, END)

    # count=0
    occurences=t.upper().count(findString.upper())
    if t.upper().count(findString.upper()) > 0:
        label = messagebox.showinfo("RESULTS",findString +'has multiple occurences' + ""+ str(occurences))
    else:
        label = messagebox.showinfo('has nooccurences')

    print(t.upper().count(findString.upper()))

#=======================================================================================================================
def cut(event=None):
    text.event_generate("<<Cut>>")

def copy(event=None):
    text.event_generate("<<Copy>>")

def paste(event=None):
    text.event_generate("<<Paste>>")

def delete(event=None):
    text.delete(0.0,END)

def undo(event=None):
    text.edit_undo()

def redo(event=None):
    text.edit_redo()

def selectAll(event=None):
    text.tag_add('sel','0.0','end')
    return'break'
def deselectAll(event=None):
    text.tag_remove('sel',0.0,'end')
    return 'break'


def tim():
    ti=time.gmtime()
    text.clipboard_append(time.asctime(ti))
    text.event_generate("<<Paste>>")

def colors():
        (triple, color) = askcolor()
        if color:
            text.config(foreground=color)

def normal():
    text.config(font=("Times New Roman", 12))

def bold():
    text.config(font=("Times New Roman", 12, "bold"))

def italic():
    text.config(font=("Times New Roman", 12, "italic"))

def underline():
    text.config(font=("Times New Roman", 12, "underline"))

def background():
    (triple, color) = askcolor()
    if color:
        text.config(background=color)

def help():
    print("Help index")
#================================================================================================================================

master=Tk()
master.iconbitmap('icons/favicon.ico')
scrollbar=Scrollbar(master)
master.title("TEXT EDITOR")
icon_frame=Frame(master,bg="black")
icon_frame.pack(expand=NO,fill=X)
text=Text(master,yscrollcommand=scrollbar.set)
text.pack(expand=YES,fill=BOTH)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=text.yview())
menu=Menu(master)
master.config(menu=menu)
# filemenu=Menu(menu,tearoff=0)
# menu.add_cascade(label='file',menu=filemenu)
# filemenu.add_command(label='New',accelerator="Ctrl+N",command=new_file)
# filemenu.add_command(label='Open',accelerator="Ctrl+O",command=openfile)
# filemenu.add_command(label='Save',accelerator="Ctrl+S",command=savefile)
# filemenu.add_command(label='SaveAs',command=saveAs)
# filemenu.add_command(label='Find',accelerator="Ctrl+F",command=findin)
# filemenu.add_separator()
# filemenu.add_command(label="Quit",command=exit)
# editmenu=Menu(menu,tearoff=0)
# menu.add_cascade(label='Edit',menu=editmenu)
# editmenu.add_command(label='Undo',accelerator="Ctrl+Z",command=undo)
# editmenu.add_command(label='Redo',accelerator="Ctrl+Y",command=redo)
# editmenu.add_command(label='Cut',accelerator="Ctrl+X",command=cut)
# editmenu.add_command(label='Copy',accelerator="Ctrl+C",command=copy)
# editmenu.add_command(label='Paste',accelerator="Ctrl+V",command=paste)
# editmenu.add_command(label='Delete',accelerator="delete",command=delete)
# editmenu.add_separator()
# editmenu.add_command(label='Select All',accelerator="Ctrl+S",command=selectAll)
# editmenu.add_command(label='Deselect All',accelerator="Ctrl+D",command=deselectAll)
# editmenu.add_command(label='Time and Date',command=tim)
# formatmenu=Menu(menu,tearoff=0)
# menu.add_cascade(label='Format',menu=formatmenu)
# formatmenu.add_command(label='Colors',command=colors)
# formatmenu.add_separator()
# formatmenu.add_command(label='Font',command=normal)
# formatmenu.add_command(label='Bold',command=bold)
# formatmenu.add_command(label='Italic',command=italic)
# formatmenu.add_command(label='Underline',command=underline)
# formatmenu.add_separator()
# formatmenu.add_command(label='Background',command=background)
#
# helpmenu=Menu(menu)
# menu.add_cascade(label='Help',menu=helpmenu)
# helpmenu.add_command(label='Help',command=help)
# helpmenu.add_command(label='About',command=About)
# status=Label(master,text="PREP. to do nothing",bd=1,relief=SUNKEN,anchor=W)
# status.pack(side=BOTTOM,fill=X)
#======================================================================================================================
text.bind("<Control-N>",new_file)
text.bind("<Control-O>",openfile)
text.bind("<Control-S>",savefile)
text.bind("<Control-F>",findin)
text.bind("<Control-X>",cut)
text.bind("<Control-C>",copy)
text.bind("<Control-V>",paste)
text.bind("<Control-A>",selectAll)
text.bind("<Control-D>",deselectAll)
#=======================================================================================================================
new_file_icon = PhotoImage(file='icons/new_file.gif')

cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')

#D:\assignment\icons\cut.gif
#adding shortcut icons
icons=( 'new_file','savefile', 'cut', 'copy', 'paste','undo', 'redo')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon)).zoom(2,2)
    cmd = eval(icon)
    tool_bar = Button(icon_frame, image=tool_bar_icon, height=35,width=35, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side=LEFT)

mainloop()
