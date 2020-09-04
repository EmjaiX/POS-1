#imports
import tkinter as tk
import json
import os
#Functions
def writeJSONFile(fileName,data):
    with open(fileName, 'w') as f:
        json.dump(data, f)

def readJSONFile(fileName,):
    with open(fileName) as f:
        global data
        data = json.load(f)

#global-variables

data = []
# root = tk.Tk()

# root.mainloop()

readJSONFile("store.json")
print(data[0]["item"])