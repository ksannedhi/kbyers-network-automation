from jnpr.junos import Device
from lxml import etree
from getpass import getpass

srx1 = Device(host = "srx1.lasthop.io", user = "pyclass", password = getpass())
srx1.open()

xml_out = srx1.rpc.get_lldp_neighbors_information()
print(etree.tostring(xml_out, encoding = "unicode"))

