from __init__ import *
import os



def l_toplevel(path = None):    
    if path is None:
        i = 0
        child = ".l" + str(i) 
        while(bool(tcl("winfo", "exists", child))):
            i = i + 1
            child = '.l' + str(i)   
        path = child
    
    tt = tkinter.Toplevel()
    tt.title(path)
    #tcl("wm", "iconphoto", tt, "-default", img_l)
    tt.wm_iconphoto(True,"::loon::loonIcon")
    #tt.iconphoto(-default img_l)
    return tt
    




if __name__ == "__main__":
    l_toplevel()
    root.mainloop()
    



    