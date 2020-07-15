"""Compare the Python "type" of the elements at ['zones-information']['zones-security']. What is the difference between the two data types? Why?"""

import xmltodict

def xml2dict(file_name):
    xml_file = open(file_name)
    xml_data = xml_file.read().strip()
    return(xmltodict.parse(xml_data))

ordered_dict1 = xml2dict("Ex1_show_security_zones.xml")
ordered_dict2 = xml2dict("Ex3_show_security_zones_trust.xml")

zones_info = ordered_dict1["zones-information"]
zones_sec = ordered_dict1['zones-information']['zones-security']

print(type(zones_info))
print(type(zones_sec))
