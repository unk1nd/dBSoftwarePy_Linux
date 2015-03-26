#!/usr/bin/python
# dB Meter software for Wensn
# by Mikael Bendiksen (c) 2015

import Tkinter
import sys
import usb.core
import sched, time
from threading import Timer
from Tkinter import *

dev = usb.core.find(idVendor=0x16c0, idProduct=0x5dc)
root = Tk()
dB = 0
labelText = StringVar()
labelText.set("0")

print "Starting dB Meter by Mikael Bendiksen"

def update():
  ret = dev.ctrl_transfer(0xC0, 4, 0, 0, 200)
  global dB
  dB = (ret[0] + ((ret[1] & 3) * 256)) * 0.1 + 30
  #print dB
  labelText.set(dB);
  root.update_idletasks() 
  t = Timer(1.0, update)
  t.start();
update()

root.title("dB Metering")
root.geometry('{}x{}'.format(600, 600))

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
rootsize = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
x = w/2 - rootsize[0]/2
y = h/2 - rootsize[1]/2
root.geometry("%dx%d+%d+%d" % ((400, 200) + (x, y)))

root.configure(background='black')

Label(root,
	text = "dB Level",
	bg = "black",
	fg = "red",
	font = "Helvetica 45 bold").pack()

Output = Label(root, 
	textvariable = labelText,
	fg = "light green",
	bg = "black",
	font = "Helvetica 72 bold")
Output.pack()

root.mainloop()

