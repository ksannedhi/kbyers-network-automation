'''Create a PyEZ Device object from the jnpr.junos Device class. This device object should connect to "srx2.lasthop.io". Use getpass() to enter the device's password.
Pretty print all of the device's facts. Additionally, retrieve and print only the "hostname" fact.'''

from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

srx1 = Device(host = "srx1.lasthop.io", user = "pyclass", password = getpass())
srx1.open()

dev_dict = srx1.facts
pprint(dev_dict)
print()
print(f"Hostname is {dev_dict['hostname']}")
