from ncclient import manager
from getpass import getpass
from pprint import pprint

netconf_mgr =  manager.connect(
    host = "srx2.lasthop.io",
    username = "pyclass",
    password = getpass(),
    port = 830,
    hostkey_verify = False,
    allow_agent = False,
    look_for_keys = False)

pprint(netconf_mgr.server_capabilities.__dict__)

