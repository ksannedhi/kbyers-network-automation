import xmltodict

def xml2dict(file_name):
    xml_file = open(file_name)
    xml_data = xml_file.read().strip()
    return(xmltodict.parse(xml_data))

ordered_dict1 = xml2dict("Ex1_show_security_zones.xml")
ordered_dict2 = xml2dict("Ex3_show_security_zones_trust.xml")

print(ordered_dict1)
print(ordered_dict2)
