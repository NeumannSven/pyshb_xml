#!/usr/bin/env python3 
#-*- coding: utf-8 -*-

from xml.etree import ElementTree as ET

sample_src = ET.parse('beispiel.xml')

#print(ET.tostring(sample_src.getroot()))

sample_root = sample_src.getroot()

frm = sample_root.find('Frame')

#new_btn = frm.find('Button')
#frm.append(new_btn)

self_btn = ET.Element('Button', x="120", y="400")
self_btn.text = "Hallo Welt!"
frm.append(self_btn)

btns = frm.findall('Button')

for btn in btns:
    print(ET.tostring(btn).decode())


sample_src.write('beispiel_new.xml')
