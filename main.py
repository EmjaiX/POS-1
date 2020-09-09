#imports
from functools import partial
import tkinter as tk
import json
import os
#Functions
def writeJSONFile(fileName,data):
    with open(fileName, 'w') as f:
        json.dump(data, f)

def readJSONFile(fileName):
    with open(fileName) as f:
        global data
        data = json.load(f)
def addToCart(item):
    print(item)
    added = False
    for x in cart:
        if x[0] == item:
            x[1] = int(x[1]) + 1
            added=True
    if not added:
        cart.append([item,1])
def checkout(cart):
    #  for item in cart:
    #     if int(item[i][1]) >0:
    sub_root = tk.Tk()
    i = 0
    has_Item = False
    for item in cart:
        if int(item[1]) >0:
            has_Item
            global data
            has_Item = True
            line = item + "   qty " + item[1] + "   $"  + float(int(item[1]) * data[]["price"])
            global total 
            total += 1
            l = tk.Label(sub_root, text=line, bg="black", fg="white" )
            l.pack(padx=5, pady=10, side=tk.TOP)
        i += 1
    line = "  Sub-Total  $" + str(total)  
    l = tk.Label(sub_root, text=line, bg="black", fg="white" )
    l.pack(padx=5, pady=10, side=tk.TOP)
    line = "  Total  $" + str(total)    
    l = tk.Label(sub_root, text=line, bg="black", fg="white" )
    l.pack(padx=5, pady=10, side=tk.TOP)
    if(has_Item):
        sub_root.mainloop()
    
def addItem():
    print()
    #append json item
def about():
    print(item)
    #append json item
    
def modstock():
    print ("hello!")

#global-variables
root = tk.Tk()
total = 0.0
data = []
cart = []
readJSONFile("store.json")

start = 2
cspan = 4
rspan = 2
padding = 5
row = start
column = start
count = 0

for item in data:
    w = tk.Button(root, text=item["item"], bg="orange", fg="blue" ,command=partial(addToCart,item["item"]))
    w.grid(row = row, column = column, columnspan = cspan, rowspan = rspan, pady = padding, padx = padding)
    column += padding
    count += 1
    if (count%5==0):
        row += padding
        column = start

w = tk.Button(root, text="Check Out", bg="white", fg="purple",command=partial(checkout,cart))
w.grid(row = row, column = column + 5 * count, columnspan = 3, rowspan = 2, pady = (20, 5), padx = 5)


menubar = tk.Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Add item", command=addItem)
filemenu.add_command(label="Modify stock", command=modstock)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)


root.mainloop()