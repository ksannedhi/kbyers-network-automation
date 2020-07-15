'''Use the findall() method to find all occurrences of "zones-security".
For each of these security zones, print out the security zone name ("zones-security-zonename", the text of that element).'''

from lxml import etree

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()
my_xml = etree.fromstring(xml_data)

zone_name_list = my_xml.findall(".//zones-security-zonename")
for zone in zone_name_list:
    print(zone.text)

print()

zones_list = my_xml.findall("./zones-security") #Alternative method
for zone in zones_list:
    print(zone.find("./zones-security-zonename").text)
