from tkinter import *
import _tkinter
from functools import partial
import sys #for sys.exit
import os



if sys.platform == "darwin":
    # OS X
    path1 = 'lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon'
    path2 = 'lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon'
elif sys.platform == "win32" or sys.platform == "cygwin":
    #Windows
    path1 = 'lappend auto_path C:/Python35/tcl/loon'
    path2 = 'lappend auto_path C:/Python35/tcl/Img'
elif sys.platform == "linux" or sys.platform == "linux2":
    #Linux
    path1 = 'lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon'
    path2 = 'lappend auto_path /usr/local/Cellar/tcl-tk/8.6.7/lib/loon'    








class input1():
    def __init__(self, parent):
        self.master = parent
        self.frame = Frame(self.master)
        self.frame.pack()        
        self.master.title("Input")
        self.usertext = StringVar()
        self.myentry = Entry(self.frame, textvariable = self.usertext).pack()
        self.mybutton = Button(self.frame, text = "Run", command = self.runClick).pack()
        self.master.grid_columnconfigure(0, weight=1)    
        self.button2 = Button(self.frame, text = "Quit", command = root.destroy).pack()
        self.master.geometry("200x200")
        self.widget = None
        tcl('wm', 'iconphoto', self.master, "-default", '::loon::loonIcon') 


    def runClick(self):
        
        #stringvar.get() into string  string.split(" ") into tuples
        if self.usertext.get()[:10] == "l_toplevel":
            path = None
            if path is None:
                i = 0
                child = ".l" + str(i) 
                while(bool(tcl("winfo", "exists", child))):
                    i = i + 1
                    child = '.l' + str(i)   
                path = child
            
            tt = Toplevel()
            tt.title(path)
            tcl('wm', 'iconphoto', tt, "-default", '::loon::loonIcon') 
            self.widget = tt
        if self.usertext.get()[:6] == "resize":

            width = self.usertext.get()[7:10]
            height = self.usertext.get()[11:14]
            geo = width + "x" + height
            self.myentry = Entry(self.master, textvariable = self.usertext, width = self.master.winfo_width())
            self.widget.geometry(geo)
            
            

root = Tk()
tcl = root.tk.call
root.eval(path1)
root.eval(path2)
root.eval("package require loon")
root.eval("package require Img")
root.eval('namespace import loon::*')  
input1(root)
root.mainloop()


#TclError = _tkinter.TclError
#root = tkinter.Tk()
#tcl = root.tk.call

#def isexist(files):
    #for r,d,f in os.walk("/Library/Tex/texbin"):
        #for files in f:
            #if files == "epstopdf":
                #address = os.path.join(r,files)
                #break
    #return address



