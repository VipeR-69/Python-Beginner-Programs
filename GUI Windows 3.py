# text widget - function like a text area, you can enter multiple lines of text
# frame       - a rectangular container to group and hold widgets

from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
from turtle import width


def click():
    messagebox.showinfo(title = "Info Message Box",
                        message = 'Hello Chiyari')    
    messagebox.showwarning(title = "Warning",
                            message = "YOU HAVE A VIRUS!!!")
    messagebox.showerror(title = "ERROR!!",
                            message = "Something Went Wrong")
    
    if messagebox.askokcancel(title = "ask ok cancel", message = "Do you want to do the thing ?"):
        print("You did a thing")
    else:
        print("You canceled a thing")
    
    if messagebox.askretrycancel(title = "ask retry cancel", message = "Do you want to retry the thing ?"):
        print("You retried a thing")
    else:
        print("You canceled a thing")

    if messagebox.askyesno(title = "ask yes or no", message = "Do you like cake ?"):
        print("I like cake too")
    else:
        print("why you don't like a cake")

    answer = messagebox.askquestion(title = "Ask Question", message = "Do you like pie")
    if answer == "yes":
        print("I like pie too")
    else :
        print("Why do you not like a pie..")

    a = messagebox.askyesnocancel(title = "Ask yes no cancel", message = "Do you like to code ?", icon ="warning" )
    if a == True:
        print("You Like To Code")
    elif a == False:
        print("Chutiya hai kya ?")
    else :
        print("You have dodged the question")


def choose():
    c = colorchooser.askcolor()
    window.config(bg = c[1])       # change the background to the color you selected


def textsub():
    input = text.get("1.0",END)
    print(input)


def openfile():
    filepath = filedialog.askopenfilename(initialdir = "D:\VSC Programs\Python Programs",
                                          title = "Open File",
                                          filetypes = (("text files","*.txt"),
                                                      ("python files","*.py"),
                                                      ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()


def savefile():
    file = filedialog.asksaveasfile(initialdir = "D:\VSC Programs\Python Programs",
                                    title = "Open File",
                                    defaultextension=".txt",
                                    filetypes = [
                                        ("Text File",".txt"),
                                        ("HTML File",".html"),
                                        ("Python File",".py"),
                                        ("All File",".*")
                                    ])
    inputtext = str(text.get("1.0",END))
    #inputtext = input("Enter some Text - ")       #use this if you want to enter text from console
    file.write(inputtext)
    file.close()

def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You pasted some text")

def create():
    new_window = Toplevel()       #TopLevel() - new window 'on top' of other windows. linked to a 'bottom' window.
                                  #             if you close the bottom window then all top level windows associated with it closes also.
#    new_window = Tk()             #Tk() = new independent window
#    window.destroy()              #close out of old window

######################################################################################################


window = Tk()
#window.geometry("420x420")

button = Button(window, text = 'click me', command = click)

choose = Button(window, text = 'Click Me', command = choose)

text = Text(window,
            bg = "light yellow",
            font = ("Ink Free", 25),
            height = 8,
            width = 20,
            padx = 15,
            pady = 15,
            fg = "purple")
textbutton = Button(window, text = "Submit", command = textsub)

openbutton = Button(text = "Open", command = openfile)

savebutton = Button(text = "Save", command = savefile)

openimage = PhotoImage(file = "pizza.png")
saveimage = PhotoImage(file = "pizza.png")
exitimage = PhotoImage(file = "pizza.png")

menubar = Menu(window)
window.config(menu = menubar)

filemenu = Menu(menubar,tearoff=0,font = ("Comic sans ms",15))
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Open", command = openfile, image=openimage, compound='left')
filemenu.add_command(label = "Save", command = savefile, image=saveimage, compound='left')
filemenu.add_command(label = "Create", command = create, image=exitimage, compound='left')
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = quit, image=exitimage, compound='left')


editmenu = Menu(menubar,tearoff=0,font = ("Comic sans ms",15))
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut", command = cut)
editmenu.add_command(label = "Copy", command = copy)
editmenu.add_command(label = "Paste", command = paste)


frame = Frame(window, bg = "yellow", bd = 5, relief = RAISED)
button1 = Button(frame, text ="W", font=('arial',25), width = 3).pack(side = TOP)
button2 = Button(frame, text ="A", font=('arial',25), width = 3).pack(side = LEFT)
button3 = Button(frame, text ="S", font=('arial',25), width = 3).pack(side = LEFT)
button4 = Button(frame, text ="D", font=('arial',25), width = 3).pack(side = LEFT)


notebook = ttk.Notebook(window)       #widget that manages a collection of windows/displays

tab1 = Frame(notebook)             #new frame for tab 1
tab2 = Frame(notebook)             #new frame for tab 2
notebook.add(tab1,text = "Tab 1")
notebook.add(tab2, text = "Tab 2")
Label(tab1, text = "This is tab 1", width = 50, height = 25).pack()
Label(tab2, text = "Goodbye going at chiyari's", width = 50, height = 25).pack()


######################################################################################################


notebook.pack(expand=True, fill = "both")
button.pack()
choose.pack()
text.pack()
textbutton.pack()
openbutton.pack()
savebutton.pack()
frame.pack()

window.mainloop()