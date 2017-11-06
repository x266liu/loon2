import tkinter
from tkinter import Tk
from tkinter import ttk



def l_toplevel(path = None):
    root = tkinter.Tk()
    root.tk.eval('package require loon')
    root.tk.eval('namespace import loon::*')        
    
    if path is None:
        i = 0
        child = '.l' + str(i) 
        str1 = "winfo exists " + child
        while(bool(root.tk.eval(str1)) - 1):
            print("1")
            i = i + 1
            child = '.l' + str(i)   
        path = child
        print("11")
    
    path = "toplevel " + path
    tt = str(root.tk.eval(path))
    default = "wm" + " " + "iconphoto" + " " + tt + " " + "-default" + " " + "::loon::loonIcon"
    root.tk.eval(default)
    root.mainloop()
    return tt
    




if __name__ == "__main__":
    l_toplevel()



    