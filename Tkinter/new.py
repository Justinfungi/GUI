from tkinter import *
import os

root =Tk()
root.title("Img")
root.title("Tkinter App")

if "nt" == os.name:
    root.wm_iconbitmap(bitmap = "icon.ico")
else:
    root.wm_iconbitmap(bitmap = r"icon.xbm")

root.mainloop()
