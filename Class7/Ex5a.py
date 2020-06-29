from lxml import etree

xml_file = open("Ex5_show_version.xml", "rb")
xml_data = xml_file.read().strip()
my_xml = etree.fromstring(xml_data)

print(f'Default namespace is {my_xml.nsmap}')
