from __init__ import *
from l_toplevel import l_toplevel

def l_subwin(parent, name = "w"):
    if isinstance(parent, int):
        str1 = ".Tk.ID " + parent #?
        parent = tcl(str1)
    
    i = 0
    child = str(parent) + "." + name
    while(bool(tcl("winfo", "exists", child))):    
        i = i + 1
        child = parent + "." + name + i
    return child
 





    

