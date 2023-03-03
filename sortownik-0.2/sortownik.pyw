import os
import time
import shutil
lista = {}
size = ""
fromfolder = ""
with open('list.txt', 'r') as f:
    size = int(f.readline().strip())
    fromfolder = f.readline().strip()
    for i in f:
        i=i.strip().split(" ", 1)
        if i:
            key, val = i
            lista[key] = val
while True:
    time.sleep(1)
    for filename in os.listdir(fromfolder):
        filekey = filename.split("-")[0]
        if filekey in lista:
            file = filekey + os.path.splitext(filename)[1]
            src = os.path.join(fromfolder, filename)

            change = 1
            while not change:
                register = os.path.getatime(src)
                time.sleep(0.01)
                change = os.path.getatime(src)-register

            if os.path.getsize(src) < size:
                into = os.path.join(lista[filekey], filename)
                if not os.path.exists(lista[filekey]): os.makedirs(lista[filekey])
                shutil.move(src, into)