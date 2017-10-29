from tkinter import *
from tkinter import ttk
from l_toplevel import l_toplevel
from l_subwin import l_subwin
import sys #for sys.exit


root = tkinter.Tk()

'''
class loonPlotFactory:
    def __init__(self, factory_tclcmd, factory_path, factory_window_title="loon plot", parent = None, *therest):
        self.factory_tclcmd = factory_tclcmd
        self.factory_path = factory_path
        self.factory_window_title = "loon plot"
        self.parent = parent
    
    def lpf(self):
        new.toplevel = True
        if parent is None:
            new.toplevel = False
            parent = l_toplevel
        
        child = l_subwin(parent, factory_path)
        try:
            plot = root.tk.call(factory_tclcmd, child, *lst)
        except:   
            if new.toplevel:
                parent.destroy()    
'''            
#python notebook for making some small intro.             
def loonPlotFactory(factory_tclcmd, factory_path, factory_window_title = "loon plot", parent = None , *arg):
   new.toplevel = False
   if parent is None:
      new.toplevel = True
      parent = l_toplevel()
   
   child = l_subwin(parent, factory_path)
   try:
      empty = ""
      for x in args:
         empty = empty + x
      cmd = factory_tclcmd + child + empty
      plot = root.tk.eval(cmd)
   
   except:
      if plot == "try-error":
         if(new.toplelvel):
            parent.destroy() #? root.tkdestroy(parent)
         sys.exit(factory_window_title + " could not be created")
      
      if new.toplevel == True:
         plot.pack(fill = BOTH, expand = YES)
         parent.titile()
         root.tk.eval("bind" + parent + "<FocusIn>" + "+::loon::setLoonInspectorActiveWidget" + plot)
         root.tk.eval("bind" + parent + "<Control-KeyPress-p>" + )#?
         
      plot = chr(plot)
      plot.__dict__ = "loon"
      return plot
        
#Tk.call() tcl() in r


#root = Tk()
#root.title("loon plot")
#factory = ttk.Frame(root)
#ttk.Button(root, text = "Hello World").grid()
root.mainloop()