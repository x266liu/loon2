from __init__ import *



def l_toplevel(path = None):
    tcl = root.eval
    tcl("package require loon")
    tcl('namespace import loon::*')        
    
    if path is None:
        i = 0
        child = '.l' + str(i) 
        str1 = "winfo exists " + child
        while(stb(tcl(str1))):
            i = i + 1
            child = '.l' + str(i)   
        path = child
    
    path = "toplevel " + path
    tt = str(tcl(path))
    default = "wm" + " " + "iconphoto" + " " + tt + " " + "-default" + " " + "::loon::loonIcon"
    tcl(default)
    root.mainloop()
    return tt
    




if __name__ == "__main__":
    l_toplevel()



    