'''Using both direct indices and the getchildren() method, obtain the first child element and print its tag name.'''

from lxml import etree

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()

my_xml = etree.fromstring(xml_data)

child1 = my_xml.getchildren()[0]
print(child1.tag)
print(my_xml[0].tag) #Alternative method
