'''5a. Connect to the srx2 device. Using an RPC call, gather and pretty-print the "show version" information.
Recall that you can retrieve RPC method name by running "show version | display xml rpc" argument. Also don't forget to convert the hyphens to underscores.
Your output should match the following:
<software-information>
<host-name>srx2</host-name>
<product-model>srx110h2-va</product-model>
<product-name>srx110h2-va</product-name>
<jsr/>
<package-information>
<name>junos</name>
<comment>JUNOS Software Release [12.1X46-D35.1]</comment>
</package-information>
</software-information>

5b. Using a direct RPC call, gather the output of "show interfaces terse". Print the output to standard out.

5c. Modify the previous task to capture "show interface terse", but this time only for "fe-0/0/7". Print the output to standard out.
Use normalize=True in the RPC method call to make the output more readable. You will also need to add pretty_print=True to the etree.tostring() call.
Consequently, your code should be similar to the following:
xml_out = dev.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))'''

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
