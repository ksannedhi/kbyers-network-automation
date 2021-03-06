'''Construct a new YAML file that contains the four Arista switches.
This YAML file should contain all of the connection information need to create a pyeapi connection using the connect method. 
Using this inventory information and pyeapi, create a Python script that configures the following on the four Arista switches: 

interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}

The {{ intf_name }} should be a Loopback interface between 1 and 99 (for example Loopback99).

The {{ intf_ip }} should be an address from the 172.31.X.X address space. The {{ intf_mask }} should be either a /24 or a /30.

Each Arista switch should have a unique loopback number, and a unique interface IP address.

You should use Jinja2 templating to generate the configuration for each Arista switch.

The data for {{ intf_name }} and for {{ intf_ip }} should be stored in your YAML file and should be associated with each individual Arista device.
For example, here is what 'arista4' might look like in the YAML file:

arista4:
  transport: https
  host: arista4.lasthop.io
  username: pyclass
  port: 443
  data:
    intf_name: Loopback99
    intf_ip: 172.31.1.13
    intf_mask: 30

Use pyeapi to push this configuration to the four Arista switches.
Use pyeapi and "show ip interface brief" to display the IP address table after the configuration changes have been made.'''


import yaml
from getpass import getpass
import pyeapi
from pprint import pprint
import jinja2

with open("Ex4.yml") as f:
    devices = yaml.load(f)

password = getpass()
for device, dev_details in devices.items():
    cfg_params = dev_details.pop("data")
    dev_details["password"] = password
    connection = pyeapi.client.connect(**dev_details)
    dev = pyeapi.client.Node(connection)
   
    with open("Ex4.j2") as f:
        int_cfg = f.read()
 
    t = jinja2.Template(int_cfg)
    cfg = t.render(cfg_params)
    cfg_lines = [line.strip() for line in cfg.splitlines()]
    output = dev.config(cfg_lines)
    print(output)

with open("Ex4.yml") as f:
    devices = yaml.load(f)

for device, device_params in devices.items():
    device_params.pop("data")
    device_params["password"] = password
    connection = pyeapi.client.connect(**device_params)
    dev = pyeapi.client.Node(connection)
    output = dev.enable("show ip interface brief")
    print(output)

