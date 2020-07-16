from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

srx1 = Device(host = "srx1.lasthop.io", user = "pyclass", password = getpass())
srx1.open()

dev_dict = srx1.facts
pprint(dev_dict)
print()
print(f"Hostname is {dev_dict['hostname']}")

