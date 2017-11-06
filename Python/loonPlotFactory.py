from __init__ import *

root = tkinter.Tk()
#python notebook for making some small intro.             
def loonPlotFactory(factory_tclcmd, factory_path, factory_window_title = "loon plot", parent = None , *args):
   ''' Takes factory_tclcmd, factory_path, factory_window_title and parent and etc. arguments
       usually factory_window_title will defulat to equal "loon plot" and parent default to None'''
   new.toplevel = False
   if parent is None:
      new.toplevel = True
      parent = l_toplevel()
   
   child = l_subwin(parent, factory_path)
   try:
      str1 = ' '.join(args)
      plot = root.tk.eval(factory_tclcmd + " " + child + " " + str1)
   
   except:
      if(new.toplelvel):
         parent.destroy() 
      sys.exit(factory_window_title + " could not be created")
      
   if new.toplevel == True:
      plot.pack(fill = BOTH, expand = YES)
      parent.titile()
      root.tk.eval("bind" + parent + "<FocusIn>" + "+::loon::setLoonInspectorActiveWidget" + plot)
      root.tk.eval("bind" + parent + "<Control-KeyPress-p>" + partial(exportImageDialog, plot)())
      root.tk.eval("bind" + parent + "<Control-KeyPress-P>" + partial(exportImageDialog, plot)())
         
   plot = chr(plot)
   plot.__dict__ = "loon"
   return plot
        
#Tk.call() tcl() in r
root.mainloop()
