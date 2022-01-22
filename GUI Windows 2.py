from tkinter import *

# radio button => similar to checkbox, but you can only select one from a group
# list box     => A listing of selectable text items within it's own container


window = Tk()
#window.geometry("420x420")

def order():
    if x.get() == 0:
        print("You ordered Pizza")
    elif x.get() == 1:
        print("You ordered a hamburger")
    elif x.get() == 2:
        print("You ordered hotdog")
    else:
        print("Huh ??")

def submit():
    print("The Temprature is "+str(scale.get())+" degree celcius")

def a():
    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    print("You have ordered - ")#,listbox.get(listbox.curselection()))
    for j in food:
        print(j)

def add():
    listbox.insert(listbox.size(),entry.get())
    print("You've added - ", entry.get()," to your order")

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height = listbox.size())
    #print("You removed "+str()+" from your order")

######################################################################################################

food = ["PIZZA","HAMBURGER","HOTDOG"]


pizzaimg = PhotoImage(file = 'E:\\Downloads\\pizza.png')
hamburgerimg = PhotoImage(file = 'E:\\Downloads\\pizza.png')
hotdogimg = PhotoImage(file = 'E:\\Downloads\\pizza.png')

foodimages = [pizzaimg, hamburgerimg, hotdogimg]

x = IntVar()
for i in range(len(food)):
    radio = Radiobutton(window,
                        text=food[i],         #adds text to radio buttons
                        variable = x,         #groups radiobuttons together if they share the same variable
                        value = i,            #assigns each radiobutton a different value
                        padx = 25,            #adds padding on x-axis
                        font = ("Impact",50),
                        image = foodimages[i],   #adds images to radioactive buttons
                        compound = 'left',    #adds image and text (left-side)
                        indicatoron = 0 ,     #eliminate circle indicator
                        width = 375,          #sets width of radio buttons
                        command = order)      #set command of radiobuttons to function
    radio.pack(anchor = W)

#hotimg = PhotoImage(file="E:\\Downloads\\flame.png")
#hotimglabel = Label(image=hotimg)
#hotimglabel.pack() 

scale = Scale(window,
              from_=0,to=100,
              length = 600,
              orient = HORIZONTAL,          #Orientation of scale (Horizontal OR Vertical)
              font = ('Consolas',20),
              tickinterval = 10,            #adds numeric indicators for value
              showvalue = 0,                 #hide current value
              resolution = 5,               #increment of slider
              troughcolor = '#69EAFF',
              fg = '#FF1C00',
              bg = '#000000',

              )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])         #set current value of slider

#coldimg = PhotoImage(file="E:\\Downloads\\snowflake.png")
#coldimglabel = Label(image=coldimg)
#coldimglabel.pack()

button = Button(window,
                text = "Submit",
                command = submit)


listbox = Listbox(window,
                  bg = "#F7FFDE",
                  font =('Constantania',30),
                  width = 10,
                  selectmode = MULTIPLE,)             #selection mode (multiple OR single)

listbox.insert(1,"Pizza")
listbox.insert(2,"Burger")
listbox.insert(3,"Pasta")
listbox.insert(4,"Garlic Bread")
listbox.insert(5,"Soup")

listbox.config(height = listbox.size())

entry = Entry(window)
addbutton = Button(window,text = "Add",command = add)

submitbut = Button(window,text = "Submit",command = a)

deletebutton = Button(window,text = "Delete",command = delete)

########################################################################################################

scale.pack()
button.pack()
listbox.pack()
entry.pack()
addbutton.pack()
submitbut.pack()
deletebutton.pack()
window.mainloop()