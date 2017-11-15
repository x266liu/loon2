from __init__ import *




def l_toplevel(path = None):      
    if path is None:
        i = 0
        child = ".l" + str(i) 
        while(stb(child.winfo_exists())):
            i = i + 1
            child = '.l' + str(i)   
        path = child
    
    tt = str(toplevel.title(path))
    
    tt.wm_iconphotor(default="::loon::loonIcon")
    return tt
    




if __name__ == "__main__":
    l_toplevel()
    root.mainloop()



    