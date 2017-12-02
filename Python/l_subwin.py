from __init__ import *

def l_subwin(parent, name = "w"):
    i = 0
    child = str(parent) + "." + name
    while(bool(tcl("winfo", "exists", child))):    
        i = i + 1
        child = parent + "." + name + i
    return child
 





    

