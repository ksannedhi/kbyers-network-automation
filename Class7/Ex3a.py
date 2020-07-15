'''Open the following two XML files: Ex1_show_security_zones.xml and Ex3_show_security_zones_trust.xml.
Use a generic function that accepts an argument "filename" to open and read a file. Inside this function, use xmltodict to parse the contents of the file.
Your function should return the xmltodict data structure. Using this function, create two variables to store the xmltodict data structure from the two files.'''

import xmltodict

def xml2dict(file_name):
    xml_file = open(file_name)
    xml_data = xml_file.read().strip()
    return(xmltodict.parse(xml_data))

ordered_dict1 = xml2dict("Ex1_show_security_zones.xml")
ordered_dict2 = xml2dict("Ex3_show_security_zones_trust.xml")

print(ordered_dict1)
print(ordered_dict2)
