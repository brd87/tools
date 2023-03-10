import os
import time
import shutil
import json
roaming = os.getenv('APPDATA')
data = {}
with open(roaming+'\sortownik\list.json', 'r') as f:
    data = json.load(f)
with open(roaming + '\sortownik\list.json', 'w') as f:
        data.update({"pid": os.getpid()})
        json.dump(data, f)
while True:
    time.sleep(1)
    for filename in os.listdir(data["download"]):
        filekey = filename.split("-")[0]
        if filekey in data["list"]:
            file = filekey + os.path.splitext(filename)[1]
            src = os.path.join(data["download"], filename)

            change = 1
            while not change:
                register = os.path.getatime(src)
                time.sleep(0.01)
                change = os.path.getatime(src)-register

            if os.path.getsize(src) < data["size"]:
                into = os.path.join(data["list"][filekey], filename)
                os.makedirs(data["list"][filekey], exist_ok=True)
                shutil.move(src, into)