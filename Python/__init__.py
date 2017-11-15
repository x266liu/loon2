import tkinter
from tkinter import *
from helper import *
from functools import partial
import sys #for sys.exit

root = tkinter.Tk()
tcl = root.eval
tcl("package require loon")
tcl('namespace import loon::*')  
