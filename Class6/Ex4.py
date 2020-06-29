from Ex2b_my_funcs import yaml_load
from getpass import getpass
import pyeapi
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

devices = yaml_load(file_name = "Ex4.yml")

password = getpass()
dev_list = []

for device_name, device_params in devices.items():
    cfg_params = device_params.pop("data")
    device_params["password"] = password
    
    env = Environment(undefined = StrictUndefined)
    env.loader = FileSystemLoader(".")

    t = env.get_template("Ex4.j2")
    cfg = t.render(cfg_params)
    cfg_lines = [line.strip() for line in cfg.splitlines()]
    
    connection = pyeapi.client.connect(**device_params)
    device = pyeapi.client.Node(connection)
    dev_list.append(device)
    output = device.config(cfg_lines)
    print(output)

for device in dev_list:
    output = device.enable("show ip interface brief")
    print(output)

