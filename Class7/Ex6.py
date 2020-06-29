import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(host =  "nxos1.lasthop.io", username = "pyclass", password = getpass(), transport = "https", port = 8443,
                api_format = "jsonrpc", verify = False)

output = device.show("show interface Ethernet1/1")
print(f"Interface: {output['TABLE_interface']['ROW_interface']['interface']}; "
      f"State: {output['TABLE_interface']['ROW_interface']['admin_state']}; "
      f"MTU: {output['TABLE_interface']['ROW_interface']['eth_mtu']}")

