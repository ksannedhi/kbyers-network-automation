'''Load the Ex5_show_version.xml file (originally from a Cisco NX-OS device) using the etree.fromstring() method.
Note this XML document, unlike the previous documents, contains the document encoding information.
Because the document encoding is at the top of the file, you will need to read the file using "rb" mode (the "b" signifies binary mode).
Print out the the namespace map of this XML object. You can accomplish this by using the .nsmap attribute of your XML object.'''

from lxml import etree

xml_file = open("Ex5_show_version.xml", "rb")
xml_data = xml_file.read().strip()
my_xml = etree.fromstring(xml_data)

print(f'Default namespace is {my_xml.nsmap}')
