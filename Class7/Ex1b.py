from lxml import etree

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()

my_xml = etree.fromstring(xml_data)

my_str = etree.tostring(my_xml)
print(my_str.decode())
print("#" * 90)
print(etree.tostring(my_xml, encoding = "unicode"))

