import xmltodict
from pprint import pprint

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()

xml_dict = xmltodict.parse(xml_data)

pprint(xml_dict)
print(type(xml_dict))

