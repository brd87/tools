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
root.geometry("300x300")
root.title("Sortownik Launcher")

size_label = tk.Label(root, text="Options\n")
size_label.pack()

size_label = tk.Label(root, text="Set maximum size in bytes:")
size_label.pack()
size_entry = tk.Entry(root)
size_entry.pack()

download_label = tk.Label(root, text="Set the directory for sorting:")
download_label.pack()
download_entry = tk.Entry(root)
download_entry.pack()

host_label = tk.Label(root, text="Set host name:")
host_label.pack()
host_entry = tk.Entry(root)
host_entry.pack()
hostd_label = tk.Label(root, text="Set host directory:")
hostd_label.pack()
hostd_entry = tk.Entry(root)
hostd_entry.pack()

list_options = [""] + list(data["list"].keys())
list_label = tk.Label(root, text="Select host to remove:")
list_label.pack()
selected_host = tk.StringVar(root)
selected_host.set(list_options[0]) 
list_dropdown = tk.OptionMenu(root, selected_host, *list_options)
list_dropdown.pack()

def save_data():
    print("inside save")
    if size_entry.get()!="":
        size = int(size_entry.get())
        data["size"] = size
    if download_entry.get()!="":
        download = download_entry.get()
        data["download"] = download
    if hostd_entry.get()!="" and host_entry.get()!="":
        host = host_entry.get()
        hostd = hostd_entry.get()
        if host in data["list"]: data["list"][host] = hostd
        else: data["list"].update({host: hostd})
    if selected_host.get()!="": del data["list"][selected_host.get()]
    with open(roaming + "\sortownik\list.json", "w") as f:
        json.dump(data, f)

def reset():
    subprocess.run(['taskkill', '/F', '/T', '/PID', str(data["pid"])])
    subprocess.Popen(["pythonw", roaming+"\Microsoft\Windows\Start Menu\Programs\Startup"+"\sortownik.pyw"])


save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack()

reset_button = tk.Button(root, text="Reset Sortownik", command=reset)
reset_button.pack()

root.mainloop()
