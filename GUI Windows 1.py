from tkinter import *

# Widgets => GUI elements:- buttons, textbooks, labels, images
# Windows => serves as a container to hold or contain these widgets
# label   => an area widget that holds text and/or an image within a window
# button  => you click it, then it does stuff
# entry widget  =>  textbox that accepts a single line of user input


def click():
    global count
    print("You clicked the button!!")
    count += 1
    print(count)

def submit():
    username = entry.get()
    print("Hello ", username)
 #  entry.config(state = DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

def password():
    p = passw.get()
    print("Password - ",p)

def display():
    if(x.get() == 1):
        print("You Agree")
    else :
        print("You Don't Agree")


###################################################################################################


window = Tk()             # instantiate an instance of a window
window.geometry("420x420")            # to adjust size of the window
window.title("Captains Esports GUI Program")      #change the title of window

icon = PhotoImage(file='D:\CyberChiyari.png')
window.iconphoto(True,icon)               # set icon of window

window.config(background="#000000")       # change the window background color (color name / hexadecimal value)

label = Label(window,
             text = "Hello Soldier",
             font = ('Arial',40,'bold','italic','underline'),
             fg = '#00ff00', 
             bg = 'black',
             relief = RAISED,
             bd = 10,
             padx = 20,
             pady = 20,
             image = icon,
             compound = 'bottom',
             )

count = 0
photo = PhotoImage(file='E:\Downloads\pixel.png')

button = Button(window,
                text='Click Me',
                command = click,
                font = ("Comic Sans",30),
                fg = "#00FF00",
                bg = 'white',
                activeforeground = "#00FF00",
                activebackground = "Black",
                state = ACTIVE,
                image = photo,
                compound = "bottom")

entry = Entry(window,
              font = ("Comic sans ms",30),
              fg = "#00ff00",
              bg = "#000000",)
entry.insert(0,"Enter your username")

passw = Entry(window,
              font = ("Comic sans ms",30),
              fg = "#00ff00",
              bg = "#000000",
              show = "*")
passw.insert(0,"password")

x = IntVar()                                                    # CheckBox Or CheckButton
pyth_photo = PhotoImage(file = "E:\Downloads\person.png")
check = Checkbutton(window,
                    text = "I agree to terms & conditions",
                    variable = x,
                    onvalue = 1,
                    offvalue = 0,
                    command = display,
                    font = ('Arial',20),
                    fg = "#00FF00",
                    bg = "#000000",
                    activeforeground = "#00FF00",
                    activebackground = "black",
                    padx = 15,
                    pady = 5,
                    image = pyth_photo,
                    compound = BOTTOM)



################################################################################################


submit = Button(window, text = "Submit", command = submit)
delete = Button(window, text = "Delete", command = delete)
backspace = Button(window, text = "Backspace", command = backspace)
password = Button(window, text = "Submit Pass", command = password)


submit.pack(side = BOTTOM)
delete.pack(side = BOTTOM)
backspace.pack(side = BOTTOM)
password.pack(side = BOTTOM)
passw.pack(side = LEFT)
entry.pack(side = LEFT)
check.pack()
button.pack()
#label.place(x=100,y=50)                # change postion of label
label.pack()


window.mainloop()          # place window on computer screen, listen for events