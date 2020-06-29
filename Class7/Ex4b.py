from lxml import etree

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()
my_xml = etree.fromstring(xml_data)

first_sec_zonename = my_xml.find("./zones-security/zones-security-zonename")
print(first_sec_zonename.text)

