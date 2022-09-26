from ast import Import
from doctest import master
from time import time


import time 
import sys
from tkinter import Tk
from tkinter import Label

master = Tk()
master.title("Digital clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S:%p$$%F")
    clock.config(text=timeVar)
    clock.after(200,get_time)
clock = Label(master, font =("Comic Sans MS", 60),bg="Blue",fg="pink")
clock.pack()
get_time()
master.mainloop()