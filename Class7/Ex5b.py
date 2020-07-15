'''Similar to earlier exercises, use the find() method to access the text of the "proc_board_id" element (serial number).
As this XML object contains namespace data, you will need to use the {*} namespace wildcard in the find() method. Your find call should look as follows:
find(".//{*}proc_board_id")

The {*} is a namespace wildcard and says to match ALL namespaces.'''

from lxml import etree

xml_file = open("Ex5_show_version.xml", "rb")
xml_data = xml_file.read().strip()
my_xml = etree.fromstring(xml_data)

ser_num = my_xml.find(".//{*}proc_board_id")
print(ser_num.text)
