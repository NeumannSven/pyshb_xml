#!/usr/bin/env python3 
#-*- coding: utf-8 -*-

from xml.etree import ElementTree as ET
from tkinter import Tk, Frame, Button

import tkinter
from applikation_commands import *

res_file = ET.parse('beispiel.xml')
root = res_file.getroot()
window = Tk()

window.title(root.attrib['title'])
window.geometry= f"{root.attrib['width']}x{root.attrib['height']}+{root.attrib['x']}+{root.attrib['y']}"


frame = root.find('Frame')
win_frm = Frame(window)
win_frm.pack()


#def drucke():
#    print("Hallo Welt!")

#def beenden():
#    window.destroy()

#def cmd_btn1():
#    print("Button 1 gedrückt")

buttons = frame.findall('Button')
win_btns = []
for button in buttons:
    btn = Button(win_frm, text=button.text)
    #btn.pack()
    btn.grid(row=int(button.attrib['row']), column=int(button.attrib['column']))
    
    try:
        button.attrib['cmd']
        btn['command'] = eval(button.attrib['cmd'])
    except:
        pass
    win_btns.append(btn)


window.mainloop()

