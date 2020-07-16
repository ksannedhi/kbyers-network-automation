from jnpr_devices import srx1
from lxml import etree
from jnpr.junos import Device

srx1 = Device(**srx1)
srx1.open()

sw_ver = srx1.rpc.get_software_information()
print(etree.tostring(sw_ver, pretty_print = True, encoding = "unicode"))

intf_data = srx1.rpc.get_interface_information(terse = True)
print(etree.tostring(intf_data, pretty_print = True, encoding = "unicode"))

fe007_data = srx1.rpc.get_interface_information(interface_name = "fe-0/0/7", normalize = True, terse = True)
print(etree.tostring(fe007_data, pretty_print = True, encoding = "unicode"))

