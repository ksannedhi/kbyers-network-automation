from ncclient import manager
from getpass import getpass

netconf_mgr = manager.connect(
    host = "srx2.lasthop.io",
    username = "pyclass",
    password = getpass(),
    port = 830,
#   device_params = {"name": "junos"},
    hostkey_verify = False,
    allow_agent = False,
    look_for_keys = False)

config = netconf_mgr.get_config(source = "running")
config_xml = config.data_xml

print(config)

