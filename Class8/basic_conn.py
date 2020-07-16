from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

srx1 = (Device(host = "srx1.lasthop.io", user = "pyclass", password = getpass())).open()
pprint(srx1.facts)

