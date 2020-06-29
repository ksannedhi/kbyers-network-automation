from lxml import etree

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()
my_xml = etree.fromstring(xml_data)

print("Tag of the first zones-security element")
print("-" * 38)
first_sec_zone = my_xml.find("./zones-security")
print(first_sec_zone.tag)

print()

print("Tag of all child elements of the first zones-security element")
print("-" * 61)
for child in first_sec_zone.getchildren():
    print(child.tag)

