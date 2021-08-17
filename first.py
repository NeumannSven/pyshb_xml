#!/usr/bin/env python3 
#-*- coding: utf-8 -*-

from xml.etree import ElementTree as ET


xmlstr = """
<html>
    <head>
        <title>Meine Seite</title>
    </head>

    <body>
        <h1>Hallo Welt!</h1>
        <h1>Noch eine Ueberschrift</h1>
    </body>

</html>
"""

html = ET.fromstring(xmlstr)

print(html)

body = html.find('body')
print(body)

#newelm = ET.SubElement(body, 'h1')
newelm = ET.Element('h1')
newelm.text = "Neuer H1 Text"

body.append(newelm)

h1 = html.findall('body/h1')

print(h1)
for i in h1:
    print(i.text)

with open('test.xml', 'w') as xmlfile:
    xmlfile.write(ET.tostring(html).decode())

