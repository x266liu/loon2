
import __init__

#change name into tki
root = tkinter.Tk()
root.tk.eval('package require loon')


#copy loon library into python36/tcl
root.tk.eval('package require Img')
root.tk.eval('package require Tk')
#http://www.posoft.de/html/extTkImg.html download win64
#root.tk.eval('source {C:/Python36/tcl/loon/demos/data/iris.tcl}')
#root.tk.eval('source {C:/Python36/tcl/loon/demos/data/olive.tcl}')



#root.tk.eval('namespace import loon::*')
#basic plot
#a = "plot -x {1 2 3} -y {3 2 1}" 
args =[" -color ", "{red orange blue} -size ", "{1.4 5.2 4}"]
#b = ""
#for x in args:
    #   b = b + x
#print(b)
#c = root.tk.eval(a)

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
#root.tk.eval('set l_p [$p layer polygon -x {0 1 2 3 3 2.5 1.5 0} -y {5 4.5 4.5 5 7 7 5.5 5.2} -color black -linecolor orange -linewidth 5]')

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
print(bool(root.tk.eval("winfo exists .l0")))

path = "toplevel .l0"
tt = list(root.tk.eval(path))
root.mainloop()
