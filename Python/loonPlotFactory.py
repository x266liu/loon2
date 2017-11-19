from __init__ import *
from l_toplevel import l_toplevel
from l_subwin import l_subwin

#python notebook for making some small intro.             
def loonPlotFactory(factory_tclcmd, factory_path, factory_window_title = "loon plot", parent = None , *args):
   ''' Takes factory_tclcmd, factory_path, factory_window_title and parent and etc. arguments
       usually factory_window_title will defulat to equal "loon plot" and parent default to None'''
   new_toplevel = False
   if parent is None:
      new_toplevel = True
      parent = l_toplevel()
   
   child = l_subwin(parent, factory_path)
   try:
      str1 = ' '.join(args)
      plot = tcl(factory_tclcmd, child)
   
   except TypeError:
      if(new_toplevel):
         tcl("destroy", parent)
      sys.exit(factory_window_title + " could not be created")
      
   if new_toplevel == True:
      plot.pack(fill = BOTH, expand = YES)
      parent.titile()
      tcl("bind", parent, "<FocusIn>", "+::loon::setLoonInspectorActiveWidget", plot)
      tcl("bind", parent, "<Control-KeyPress-p>", partial(exportImageDialog, plot)())
      tcl("bind", parent, "<Control-KeyPress-P>", partial(exportImageDialog, plot)())
         
   plot = str(plot)
   #plot.__dict__ = "loon"
   return plot
        

def ask_for_userinput():
   user_input = raw_input("Give me your command! Just type \"exit\" to close: ")
   if user_input == "exit":
      ROOT.quit()
   else:
      label = Label(ROOT, text=user_input)
      label.pack()
      ROOT.after(0, ask_for_userinput)

parent = l_toplevel()
loonPlotFactory("::loon::plot", "plot", "loon scatterplot", parent)
root.mainloop()