from __init__ import *



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
    tt.wm_iconphoto(True,"::loon::loonIcon")
    return str(tt.title())
    




    



    