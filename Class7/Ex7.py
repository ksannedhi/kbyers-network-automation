import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(host =  "nxos2.lasthop.io", username = "pyclass", password = getpass(), transport = "https", port = 8443,
                api_format = "xml", verify = False)

output = device.show("show interface Ethernet1/1")
print(f'Interface: {output.find(".//interface").text}; '
        f'State: {output.find(".//state").text}; '
        f'MTU: {output.find(".//eth_mtu").text}')

print()

show_output = device.show_list(["show system uptime", "show system resources"])
for output in show_output:
    print(etree.tostring(output, encoding = "unicode"))
    print()

conf_cmds = [
    "interface loopback180",
    "description loopback180",
    "no shutdown",
    "interface loopback189",
    "description loopback189",
    "no shutdown",
]

conf_output = device.config_list(conf_cmds)
for cmd in conf_output:
   print(etree.tostring(cmd, encoding = "unicode"))

