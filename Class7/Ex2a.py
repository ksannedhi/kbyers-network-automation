'''Using xmltodict, load the Ex1_show_security_zones.xml file as a Python dictionary. Print out this new variable and its type.
Note, the newly created object is an OrderedDict; not a traditional dictionary.'''

import xmltodict
from pprint import pprint

xml_file = open("Ex1_show_security_zones.xml")
xml_data = xml_file.read().strip()

xml_dict = xmltodict.parse(xml_data)

pprint(xml_dict)
print(type(xml_dict))

