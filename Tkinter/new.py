from tkinter import *


root =Tk()
root.title("Password")
#root.geometry("500x500")

e= Entry(root, width=35, bg="#EEB462", borderwidth=4)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)


def button_click(number):
    print(number)
    e.delete(0, END)
    e.insert(0, number)


#solution online

BoardValue = ["1","2","3","4","5","6","7","8","9","0"]
for i, b in enumerate(BoardValue):
    row = int(i/3)+1
    col = i%3
    btn = Button(root, text=b,padx=40, pady=20, command= lambda i=i+1: button_click(i))
    btn.grid(row=row, column=col)

'''
for i, b in enumerate(BoardValue):
    if i%3 == 0:
        row_frame = Frame(root)
        row_frame.pack(side="top")
    btn = Button(row_frame, text=b, relief=GROOVE, width=2)
    btn.pack(side="left")
'''

button_add = Button(
                        root, text="Add",
                        padx=30, pady=20,
                        command= lambda: button_click(10))
button_clear = Button(
                        root, text="Clear",
                        command= button_add)
button_equal = Button(
                        root, text="Equal",
                        command= button_add)
button_clear.grid(row=4, column=1, sticky="nsew", columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, sticky="nsew", columnspan=2)
root.mainloop()
