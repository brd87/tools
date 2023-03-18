import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import datetime
import os

root = tk.Tk()
root.geometry("340x170")
root.title("Settings")

textp = tk.Label(root, text="Options\n")
textp.pack()


frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP)
frame2 = tk.Frame(root)
frame2.pack(side=tk.TOP)
frame3 = tk.Frame(root)
frame3.pack(side=tk.TOP)

textp = tk.Label(frame1, text="Choose base image:")
textp.pack(side=tk.LEFT)
baseimgI = tk.Entry(frame1)
baseimgI.pack(side=tk.LEFT)
base = tk.Button(frame1, text="Explore", command=lambda: baseimgI.insert(0, askopenfilename()))
base.pack(side=tk.LEFT)

textp = tk.Label(frame2, text="Choose image to merge:")
textp.pack(side=tk.LEFT)
mergeI = tk.Entry(frame2)
mergeI.pack(side=tk.LEFT)
merge = tk.Button(frame2, text="Explore", command=lambda: mergeI.insert(0, askopenfilename()))
merge.pack(side=tk.LEFT)

list_options = ["Bottom", "Top", "Right", "Left"]
textp = tk.Label(frame3, text="Merging side:")
textp.pack(side=tk.LEFT)
selectI = tk.StringVar(root)
selectI.set(list_options[0]) 
list_dropdown = tk.OptionMenu(frame3, selectI, *list_options)
list_dropdown.pack(side=tk.LEFT)

def merge_img():
    if baseimgI.get()!="" and mergeI.get()!="" and selectI.get()!="":
        img1 = Image.open(baseimgI.get())
        img2 = Image.open(mergeI.get())
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        if selectI.get()=="Bottom":
            newimg = Image.new(mode="RGBA", size=(max(img1.width, img2.width), img1.height+img2.height))
            newimg.paste(img1, (0,0))
            newimg.paste(img2, (0,img1.height))
            newimg.save('merged-'+timestamp+'.png')
        if selectI.get()=="Top":
            newimg = Image.new(mode="RGBA", size=(max(img1.width, img2.width), img1.height+img2.height))
            newimg.paste(img2, (0,0))
            newimg.paste(img1, (0,img2.height))
            newimg.save('merged-'+timestamp+'.png')
        if selectI.get()=="Right":
            newimg = Image.new(mode="RGBA", size=(img1.width+img2.width, max(img1.height, img2.height)))
            newimg.paste(img1, (0,0))
            newimg.paste(img2, (img1.width, 0))
            newimg.save('merged-'+timestamp+'.png')
        if selectI.get()=="Left":
            newimg = Image.new(mode="RGBA", size=(img1.width+img2.width, max(img1.height, img2.height)))
            newimg.paste(img2, (0,0))
            newimg.paste(img1, (img2.width, 0))
            newimg.save('merged-'+timestamp+'.png')
run = tk.Button(root, text="Merge", command=merge_img)
run.pack()

root.mainloop()