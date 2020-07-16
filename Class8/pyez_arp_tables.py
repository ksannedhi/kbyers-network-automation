from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
from getpass import getpass
from pprint import pprint

srx2 = Device(host = "srx2.lasthop.io", user = "pyclass", password = getpass())
srx2.open()

arp_entries = ArpTable(srx2)
arp_entries.get()

print(arp_entries)
print(arp_entries.keys())
pprint(arp_entries.values())
pprint(arp_entries.items())
