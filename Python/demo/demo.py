#example
from tkinter import *
from tkinter import ttk



def calculate(*args): 
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0) 
    except ValueError:
        pass
root = Tk()
'''
#general case
root.title("Feet to Meters")
mainframe = ttk.Frame(root, padding="3 3 12 12") 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) 
mainframe.columnconfigure(0, weight=1) 
mainframe.rowconfigure(0, weight=1)
feet = StringVar() 
meters = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) 
feet_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) 
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W) 
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E) 
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus() 
root.bind('<Return>', calculate)
'''

'''
#button case
button = ttk.Button(root, text = 'Hello', command = "buttonpressed")
button.grid(column = 1, row = 1)
#button['text'] = 'goodbye'
measureSystem = StringVar()
check = ttk.Checkbutton(root, text='Use Metric', variable=measureSystem, onvalue='metric', offvalue='imperial')
check.grid(column = 1, row = 3, sticky = W)
phone = StringVar()
English = ttk.Radiobutton(root, text='English', variable=phone, value='e') 
Chinese= ttk.Radiobutton(root, text='Chinese', variable=phone, value='c') 
Russian= ttk.Radiobutton(root, text='Russian', variable=phone, value='r')
ci = PhotoImage(file = 'A:/研究生/pp/c.gif')
ei = PhotoImage(file = 'A:/研究生/pp/u.gif')
ri = PhotoImage(file = 'A:/研究生/pp/r.gif')
c = ttk.Radiobutton(root, image = ci, variable=phone, value='c') 
e = ttk.Radiobutton(root, image = ei, variable=phone, value='e') 
r = ttk.Radiobutton(root, image = ri, variable=phone, value='r') 
English.grid(column = 2, row = 4)
Chinese.grid(column = 1, row = 4)
Russian.grid(column = 3, row = 4)
c.grid(column = 1, row = 5 )
e.grid(column = 2, row = 5)
r.grid(column = 3, row = 5)
'''

'''
#label case
label = ttk.Label(root, text='Full name: ')
resultsContents = StringVar() 
label1 = ttk.Label(root)
label1['textvariable'] = resultsContents 
resultsContents.set('New value to display')
label.grid(column = 1, row = 1, sticky = E)
label1.grid(column = 2, row = 2, sticky = W)
label2 = ttk.Label(root)
image = PhotoImage(file = 'A:/研究生/pp/wing.gif') 
label2['image'] = image
label2.grid(column = 3, row = 3, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)
'''

#combobox
countryvar = StringVar()
country = ttk.Combobox(root, textvariable=countryvar)
country['values'] = ('中国', 'USA', 'Россия')
country.grid()

root.mainloop()