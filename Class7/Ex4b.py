'''Use the find() method to find the first "zones-security-zonename". Print out the zone name for that element (the "text" of that element).'''

from lxml import etree

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()
my_xml = etree.fromstring(xml_data)

first_sec_zonename = my_xml.find("./zones-security/zones-security-zonename")
print(first_sec_zonename.text)
