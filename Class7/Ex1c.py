'''Print out the root element tag name (this tag should have a value of "zones-information").
Print the number of child elements of the root element (you can retrieve this using the len() function).'''

from lxml import etree

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()

my_xml = etree.fromstring(xml_data)

print(my_xml.tag)
print(len(my_xml.getchildren()))
print(len(my_xml)) #Alternative method
