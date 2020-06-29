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

