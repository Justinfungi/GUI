from tkinter import *


root =Tk()

e= Entry(root, width=50, bg="#EEB462", borderwidth=4)
e.pack()
e.insert(0,"Enter your name: ")

def myclick():
    mylabel = Label(root, text="Hello"+e.get(),fg="#534666",bg="#CD7672")
    mylabel.pack()

but_text = "love you, enter your lovely name"
mybutton = Button(
                    root, text=but_text,
                    padx =25, pady=10, command = myclick,
                    fg="#138086",bg="#DC8665"
                    )
mybutton.pack()

root.mainloop()
