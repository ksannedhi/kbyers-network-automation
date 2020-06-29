import yaml
from netmiko import ConnectHandler
from os import path

hw_dir = path.expanduser("~")
file_name = path.join(hw_dir, ".netmiko.yml")

with open(file_name) as f:
    dev_data = yaml.load(f)

cisco3_dict = dev_data["cisco3"]
cisco3_connect = ConnectHandler(**cisco3_dict)
print(cisco3_connect.find_prompt())

