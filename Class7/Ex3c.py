import xmltodict

def xml2dict_forcelist(file_name, force_list = None):
    xml_file = open(file_name)
    xml_data = xml_file.read().strip()
    return(xmltodict.parse(xml_data, force_list = force_list))

ordered_dict1 = xml2dict_forcelist("Ex3_show_security_zones_trust.xml", force_list={"zones-security": True})
zones_security1 = ordered_dict1['zones-information']['zones-security']
print(type(zones_security1))

print()

ordered_dict2 = xml2dict_forcelist("Ex3_show_security_zones_trust.xml")
zones_security2 = ordered_dict2['zones-information']['zones-security']
print(type(zones_security2))

