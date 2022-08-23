from tkinter import *


root =Tk()

e= Entry(root, width=50, bg = "#EEB462")
e.pack()

def myclick():
    mylabel = Label(root, text="love you zdm, click me",fg="#534666",bg="#CD7672")
    mylabel.pack()

mybutton = Button(
                    root, text="love you",
                    padx =25, pady=10, command = myclick(),
                    fg="#138086",bg="#DC8665"
                    )
mybutton.pack()

root.mainloop()
