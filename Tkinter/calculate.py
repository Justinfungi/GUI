from tkinter import *


root =Tk()
root.title("Password")
#root.geometry("500x500")

e= Entry(root, width=35, bg="#EEB462", borderwidth=4)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)


def button_click(number):
    print(number)
    #
    current = e.get()
    e.delete(0, END)
    e.insert(0, int(str(current)+str(number)))

def button_clear():
    e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)


def button_equal():
	second_number = int(e.get())
	e.delete(0, END)

	if math == "addition":
		e.insert(0, f_num + second_number)

	if math == "subtraction":
		e.insert(0, f_num - second_number)

	if math == "multiplication":
		e.insert(0, f_num * second_number)

	if math == "division":
		e.insert(0, f_num / second_number)

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)

#solution online

BoardValue = ["1","2","3","4","5","6","7","8","9","0"]
for i, b in enumerate(BoardValue):
    row = int(i/3)+1
    col = i%3
    if i==9:
        btn = Button(root, text=b,padx=40, pady=20, command= lambda i=i+1: button_click(0))
    else:
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
                        command= button_add)
button_clear = Button(
                        root, text="Clear",
                        command= button_clear)
button_equal = Button(
                        root, text="Equal",
                        command= button_equal)
button_subtract = Button(
                        root, text="Sub",
                        padx=41, pady=20,
                        command=button_subtract)
button_multiply = Button(
                        root, text="Mul",
                        padx=40, pady=20,
                        command=button_multiply)
button_divide = Button(
                        root, text="Div",
                        padx=41, pady=20,
                        command=button_divide)

button_clear.grid(row=4, column=1, sticky="nsew", columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, sticky="nsew", columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
