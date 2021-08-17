from xml.etree import ElementTree as ET
import os

res_file = ET.parse('beispiel.xml')
root = res_file.getroot()
frame = root.find('Frame')

buttons = frame.findall('Button')
code = """
# Code generated by codegen

"""

if not os.path.exists('applikation_commands.py'): 
    for button in buttons:
        try:
            button.attrib['cmd']
            code += f"""
def {button.attrib['cmd']}():
    print('{button.text} gedrückt')
"""
        except:
            pass


    with open('applikation_commands.py', 'w') as cmd_file:
        cmd_file.write(code)

