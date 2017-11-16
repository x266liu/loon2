import tkinter
#from functools import partial
#import sys #for sys.exit
import os


root = tkinter.Tk()
tcl = root.tk.call
root.eval('lappend auto_path C:/Python35/tcl/loon')
root.eval('lappend auto_path C:/Python35/tcl/Img')
root.eval("package require loon")
root.eval("package require Img")
root.eval('namespace import loon::*')  

