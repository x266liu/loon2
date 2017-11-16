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
    #tt.wm_iconphoto(True,img_l)
    #tt.iconphoto(-default img_l)
    return tt
    




if __name__ == "__main__":
    icon_fname1 = '/Users/x266liu/Desktop/RAY.bmp'
    print(icon_fname1)
    img_k = tkinter.PhotoImage(file=icon_fname1)
    print(img_k)
    tt= l_toplevel()
    tt.wm_iconwindow(icon_fname1)
    #root.withdraw()
    root.mainloop()
    



    