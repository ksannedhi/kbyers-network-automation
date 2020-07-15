'''Create a variable named "trust_zone". Assign this variable to be the first "zones-security" element in the XML tree.
Access this newly created variable and print out the text of the "zones-security-zonename" child.'''

from lxml import etree

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()

my_xml = etree.fromstring(xml_data)

trust_zone = my_xml[0]
print(trust_zone[0].text)
