import tkinter
import _tkinter
from functools import partial
import sys #for sys.exit
import os

TclError = _tkinter.TclError
root = tkinter.Tk()
tcl = root.tk.call




if sys.platform == "darwin":
    # OS X
    path1 = 'lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon'
    path2 = 'lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon'
elif sys.platform == "win32":
    #Windows
    path1 = 'lappend auto_path C:/Python35/tcl/loon'
    path2 = 'lappend auto_path C:/Python35/tcl/Img'
elif sys.platform == "linux" or sys.platform == "linux2":
    #Linux
    path1 = 'lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon'
    path2 = 'lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon'    



root.eval(path1)
root.eval(path2)
root.eval("package require loon")
root.eval("package require Img")
root.eval('namespace import loon::*')  


for r,d,f in os.walk("/Library"):
    for files in f:
        if files == "epstopdf":
            print(os.path.join(r,files))