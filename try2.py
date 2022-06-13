import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from itertools import count, cycle
from tkinter.ttk import *
import main
import os
import subprocess
 
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 120
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

def printSomething():
    subprocess.call(" python main.py ", shell=True)

#demo :
root = tk.Tk()
root.config(bg="lightblue")
root.title("BUDDY")
root.iconbitmap("buddyico.ico")
lbl = ImageLabel(root)
lbl.load('buddya.gif')
lbl.pack()
button = Button(root, text="CHAT WITH BUDDY", command=printSomething) 
button.pack()
lbl.pack()
root.mainloop()