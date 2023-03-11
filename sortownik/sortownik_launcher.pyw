import tkinter as tk
import os
import json
import tkinter as tk

import subprocess

roaming = os.getenv('APPDATA')
data = {}
with open(roaming + '\sortownik\list.json', 'r') as f:
    data = json.load(f)

root = tk.Tk()
root.geometry("240x290")
root.title("Settings")

text = tk.Label(root, text="Options\n")
text.pack()

text = tk.Label(root, text="Set maximum size in bytes:")
text.pack()
size = tk.Entry(root)
size.pack()

text = tk.Label(root, text="Set the directory for sorting:")
text.pack()
download = tk.Entry(root)
download.pack()

text = tk.Label(root, text="Set host name:")
text.pack()
host = tk.Entry(root)
host.pack()

text = tk.Label(root, text="Set host directory:")
text.pack()
hostd = tk.Entry(root)
hostd.pack()


text = tk.Label(root, text="Select host to remove:")
text.pack()
options = [""] + list(data["list"].keys())
select = tk.StringVar(root)
select.set(options[0]) 
list_dropdown = tk.OptionMenu(root, select, *options)
list_dropdown.pack()

def save_data():
    if size.get()!="":
        size = int(size.get())
        data["size"] = size
    if download.get()!="":
        download = download.get()
        data["download"] = download
    if hostd.get()!="" and host.get()!="":
        host = host.get()
        hostd = hostd.get()
        if host in data["list"]: data["list"][host] = hostd
        else: data["list"].update({host: hostd})
    if select.get()!="": del data["list"][select.get()]
    with open(roaming + "\sortownik\list.json", "w") as f:
        json.dump(data, f)

def reset_sortownik():
    subprocess.run(['taskkill', '/F', '/T', '/PID', str(data["pid"])])
    subprocess.Popen(["pythonw", roaming+"\Microsoft\Windows\Start Menu\Programs\Startup\sortownik.pyw"])

reset = tk.Button(root, text="Reset Sortownik", command=reset_sortownik)
reset.pack(padx=5, side=tk.RIGHT)

save = tk.Button(root, text="Save", command=save_data)
save.pack(padx=5, side=tk.LEFT)

root.mainloop()