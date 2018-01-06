from tkinter import *

window = Tk()

def close_window (): 
    window.destroy()

frame = Frame(window)
frame.pack()
button = Button (frame, text = "Good-bye.", command = close_window)
button.pack()

window.mainloop()
#import time
#from tkinter import *

#class MyApp:
    #def __init__(self, parent):
        #self.myParent = parent  ### (7) remember my parent, the root
        #self.myContainer1 = Frame(parent)
        #self.myContainer1.pack()

        #self.button1 = Button(self.myContainer1)
        #self.button1.configure(text="Button")
        #self.button1.pack()
        #self.button1.bind("<Button-1>", self.button1Click)

        #self.lbl = Label(self.myContainer1)
        #self.lbl.pack()

        #self.button2 = Button(self.myContainer1)
        #self.button2.configure(text="Quit", background="red")
        #self.button2.pack()
        #self.button2.bind("<Button-1>", self.button2Click)


    #def button1Click(self, event):    ### (3)
        ## expensive process here
        ## simulated by time.sleep
        #self.lbl.configure(text='Running command...')
        #self.myContainer1.update_idletasks()
        #time.sleep(4)
        #self.lbl.configure(text='Finished running command...')

    #def button2Click(self, event):  ### (5)
        #self.myParent.destroy()     ### (6)


#root = Tk()
#myapp = MyApp(root)
#root.mainloop()
#from __init__ import *

#change name into tki
#root.tk.eval('package require loon')


#copy loon library into python36/tcl
#root.tk.eval('package require Img')
#root.tk.eval('package require Tk')
#http://www.posoft.de/html/extTkImg.html download win64
#root.tk.eval('source {C:/Python36/tcl/loon/demos/data/iris.tcl}')
#root.tk.eval('source {C:/Python36/tcl/loon/demos/data/olive.tcl}')



#root.tk.eval('namespace import loon::*')
#basic plot
#a = "plot -x {1 2 3} -y {3 2 1} -color orange" 
#args =[" -color ", "{red orange blue} -size ", "{1.4 5.2 4}"]
'''
import os 
result = []
name = "epstopdf"
for root, dirs, files in os.walk("/Library"):
    print(root)
    if name in files:
        result.append(os.path.join(root, name))
        break
print(result)
'''
#a = [0,1,2,3,4,5,6]
#b = 0
#a.remove(0)
#print(a)
#b = ""
#for x in args:
    #   b = b + x
#print(b)
#
#other plots

#root.tk.eval('set p1 [plot -x $SepalWidth -y $PetalWidth -linkingGroup iris]')
#root.tk.eval('set p2 [plot -x $PetalLength -y $PetalWidth -linkingGroup iris]')
#root.tk.eval('set p3 [plot -x $SepalLength -y $PetalLength -linkingGroup none]')
#root.tk.eval('set h [histogram -x $SepalLength -linkingGroup iris]')

#root.tk.eval('set pa2 [plot -x {1 2 3 4 5 6 7} -y {1 2 3 4 5 6 7} -title \"A 2\"]')
#root.tk.eval('set pb2 [plot -x {1 2 3 4 5} -y {1 2 3 4 5} -title \"B 2\"]')

#root.tk.eval('set p [plot -x {0 1 2 3 4 5 6 7} -y {0 1 2 3 4 5 6 7}\
    #   -showScales TRUE -showGuides TRUE]')
#root.tk.eval('$p layer ids')
#root.tk.eval('plot polygon -x {0 1 2 3 3 2.5 1.5 0} -y {5 4.5 4.5 5 7 7 5.5 5.2}')

#root.tk.eval('$p layer use $l_p info states')
#p <- l_plot(x=0:7, y=0:7, showScales=TRUE, showGuides=TRUE,
    #xlabel='', ylabel='')

#root.tk.eval('dict for {name value} $loon::data::olive {set $name $value}')
#root.tk.eval('set h [loon::histogram -x [dict get $loon::data::olive oleic] -xlabel oleic]')

#root.tk.eval('set Area [dict get $loon::data::olive Area];')
#root.tk.eval('puts \"create Area variable\"')
#root.tk.eval('set oliveacids [dict filter $loon::data::olive script {key value} {\
            #expr {$key ni {Area Region}}}]; \
            #puts \"filter data\" ')
#root.tk.eval('set s [serialaxes -data $oliveacids -color $Area -title "olive data"]')

'''
root.tk.eval('set nodes [list A B C D E]')
root.tk.eval('set G [completegraph $nodes]')
root.tk.eval('set LG [linegraph {*}$G]')
root.tk.eval('set g [graph -nodes [lindex $LG 0] -from [lindex $LG 1]\
      -to [lindex $LG 2] -isDirected [lindex $LG 3]]')
root.tk.eval('$g navigator add ')
'''
#print(bool(root.tk.eval("winfo exists .l0")))

