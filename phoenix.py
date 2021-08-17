
from xml.etree import ElementTree as ET
xmlsrc = ET.parse("BMECAT_2005_ETIM_7.0_20210728_074623.xml")

bme_cat = xmlsrc.getroot()
catalog = bme_cat.find("T_NEW_CATALOG")
products = catalog.findall("PRODUCT")

for product in products:
    print(product.find("SUPPLIER_PID").text, end=' | ')
    print(product.find("PRODUCT_DETAILS/DESCRIPTION_SHORT").text, end=' | ')
    print(product.find("PRODUCT_DETAILS/INTERNATIONAL_PID").text, end=' | ')

    mimes = product.findall("USER_DEFINED_EXTENSIONS/UDX.EDXF.MIME_INFO/UDX.EDXF.MIME/UDX.EDXF.MIME_FILENAME")

    for mime in mimes:
        if mime.text.endswith('04.jpg'):
            print(mime.text)
            break
