from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from pprint import pprint

srx1 = Device(host = "srx1.lasthop.io", user = "pyclass", password = getpass())
srx1.open()

ports = EthPortTable(srx1)
ports.get()

print(ports)
pprint(ports.keys())
#pprint(ports.values())
#pprint(ports.items())

