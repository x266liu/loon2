from __init__ import *



def l_toplevel(path = None):      
    if path is None:
        i = 0
        child = ".l" + str(i) 
        while(bool(tcl("winfo", "exists", child))):
            i = i + 1
            child = '.l' + str(i)   
        path = child
    
    tt = str(tcl("toplevel", path))
    tcl("wm", "iconphoto", tt,  "-default", img_l)
    return tt
    




if __name__ == "__main__":
    l_toplevel()
    root.mainloop()



    