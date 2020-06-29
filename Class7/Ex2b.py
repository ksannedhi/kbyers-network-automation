import xmltodict

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()

my_dict = xmltodict.parse(xml_data)
zones_list = my_dict["zones-information"]["zones-security"]

for index, zone in enumerate(zones_list, 1):
    print(f'Security Zone #{index}: {zone["zones-security-zonename"]}')

