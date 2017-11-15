import tkinter
from tkinter import *
from helper import *
from functools import partial
import sys #for sys.exit
import os

root = tkinter.Tk()
tcl = root.tk.call
root.eval('lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon')
root.eval('lappend auto_path1 /usr/local/Cellar/tcl-tk/8.6.7/lib/Img')
icon_fname = os.path.join('/usr/local/Cellar/tcl-tk/8.6.7/lib/loon', 'images', 'LoonIcon.gif')
img_l = PhotoImage(file = icon_fname)
root.eval("package require loon")
root.eval("package require Img")
root.eval('namespace import loon::*')  
