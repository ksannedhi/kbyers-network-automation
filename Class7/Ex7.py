'''7a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be "xml" and the transport should be "https" (port 8443).
Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:
Interface: Ethernet1/1; State: up; MTU: 1500

7b. Run the following two show commands on the nxos1 device using a single method and passing in a list of commands: "show system uptime" and "show system resources".
Print the XML output from these two commands.

7c. Using the nxapi_plumbing config_list() method, configure two loopbacks on nxos1 including interface descriptions.
Pick random loopback interface numbers between 100 and 199.'''

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
