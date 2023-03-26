import tkinter as tk
import os
import json

import subprocess

roaming = os.getenv('APPDATA')
data = {}
with open(roaming + '\sortownik\list.json', 'r') as f:
    data = json.load(f)

root = tk.Tk()
root.geometry("240x290")
root.title("Settings")

textp = tk.Label(root, text="Options\n")
textp.pack()

textp = tk.Label(root, text="Set maximum size in bytes:")
textp.pack()
sizeI = tk.Entry(root)
sizeI.pack()

textp = tk.Label(root, text="Set the directory for sorting:")
textp.pack()
downloadI = tk.Entry(root)
downloadI.pack()

textp = tk.Label(root, text="Set host name:")
textp.pack()
hostI = tk.Entry(root)
hostI.pack()

textp = tk.Label(root, text="Set host directory:")
textp.pack()
hostdI = tk.Entry(root)
hostdI.pack()

list_options = [""] + list(data["list"].keys())
textp = tk.Label(root, text="Select host to remove:")
textp.pack()
selectI = tk.StringVar(root)
selectI.set(list_options[0]) 
list_dropdown = tk.OptionMenu(root, selectI, *list_options)
list_dropdown.pack()

def my_remove():
    selectI.set('')
    list_dropdown['menu'].delete(0,'end')
def my_add():
    my_remove()
    for opt in list_options: 
        list_dropdown['menu'].add_command(label=opt, command=tk._setit(selectI, opt))
    selectI.set(list_options[0])

def update_host_controls():
    hostI.delete(0,tk.END)
    hostI.insert(0,"")
    hostdI.delete(0,tk.END)
    hostdI.insert(0,"")
    my_add()

def save_data():
    global list_options
    print("inside save")

    if sizeI.get()!="":
        size = int(sizeI.get())
        data["size"] = size

    if downloadI.get()!="":
        download = downloadI.get()
        data["download"] = download

    if hostdI.get()!="" and hostI.get()!="":
        host = hostI.get()
        hostd = hostdI.get()
        
        data["list"][host] = hostd
        list_options = [""] + list(data["list"].keys())
        update_host_controls()

    if selectI.get()!="": 
        del data["list"][selectI.get()]
        list_options = [""] + list(data["list"].keys())
        update_host_controls()

    with open(roaming + "\sortownik\list.json", "w") as f:
        json.dump(data, f)

def reset_sortownik():
    subprocess.run(['taskkill', '/F', '/T', '/PID', str(data["pid"])])
    subprocess.Popen(["pythonw", roaming+"\Microsoft\Windows\Start Menu\Programs\Startup"+"\sortownik.pyw"])


reset = tk.Button(root, text="Reset Sortownik", command=reset_sortownik)
reset.pack(padx=5, side=tk.RIGHT)

save = tk.Button(root, text="Save", command=save_data)
save.pack(padx=5, side=tk.LEFT)

root.mainloop()