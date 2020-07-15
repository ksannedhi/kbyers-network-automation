'''Using the Ex1_show_security_zones.xml file, read the file contents and parse the file using etree.fromstring().
Print out the newly created XML variable and also print out the variable's type. Your output should look similar to the following:
<Element zones-information at 0x7f3271194b48>
<class 'lxml.etree._Element'>'''

from lxml import etree

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()

my_xml = etree.fromstring(xml_data)

print(my_xml)
print(type(my_xml))
