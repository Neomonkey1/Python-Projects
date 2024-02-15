from tkinter import *

#making a window
win = Tk()
#adding buttons to the window using pack()
b1 = Button(win, text = "One")
b2 = Button(win, text = "Two")
b1.pack()
b2.pack()

#declaring where the widgets(buttons, labels and whatnot) go
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3 = Button(win, text = "Three")
b3.pack(side=BOTTOM)

b3.pack(side=BOTTOM, pady=10)
b4 = Button(win, text = 'Four')
b4.pack(side= RIGHT, pady=20)

#making new window and using the grid()
win= Tk()
b1 = Button(win, text='One')
b2 = Button(win, text='Two')
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
#making label widget
l = Label(win, text='This is a label')
l.grid(row=1, column=0)

#making new window with a frame
win = Tk()
f = Frame(win)
b1 = Button(f, text='One')
b2 = Button(f, text= 'Second')
b3 = Button(f, text= 'Three')
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text='This label is over all buttons')
l.pack()
f.pack()
#using the configure()
b1.configure(text="Uno")
def but1():
    print('Button one was pushed')
b1.configure(command=but1)

#making new window and using entry(), StringVar() and get()
win = Tk()
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()
v.get()
# you can set text into StringVar
v.set("This is set by the program")

#making new window with a listbox and 'height' parameters
win = Tk()
lb = Listbox(win, height=3)
lb.pack()
lb.insert(END, 'first entry')
lb.insert(END, 'second entry')
lb.insert(END, 'third entry')
lb.insert(END, 'fourth entry')
# fourth entry doesn't show since we set height limit to 3 lines
# using scrollbar()
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)
# these functions is to make the scrollbar functional
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
# this method curselection returns what you select back to you
lb.curselection()
