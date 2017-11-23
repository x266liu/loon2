import tkinter
import _tkinter
from functools import partial
import sys #for sys.exit
import os

TclError = _tkinter.TclError
root = tkinter.Tk()
tcl = root.tk.call

#system switch

#default address of windows
root.eval('lappend auto_path C:/Python35/tcl/loon')
root.eval('lappend auto_path C:/Python35/tcl/Img')

#default address of mac os
#root.eval('lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon')
#root.eval('lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/Img')
root.eval("package require loon")
root.eval("package require Img")
root.eval('namespace import loon::*')  

