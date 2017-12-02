from __init__ import *

def l_size(widget):
     width = tcl("winfo", "width", widget)
     height = tcl("winfo", "height", widget)
     return (map(lambda x: int(x), [width, height]))
     
 


