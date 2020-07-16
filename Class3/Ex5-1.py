import yaml
from os import path
from netmiko import ConnectHandler

file_name = path.join("/home/ksannedhi/.netmiko.yml") #Alternately you can use "," in between. In that case, you don't need "/" in the file part OR + in between the directory and the filename.

with open(file_name) as f:
    dev_data = yaml.load(f)

cisco3_dict = dev_data["cisco3"]
cisco3_connect = ConnectHandler(**cisco3_dict)

print(cisco3_connect.find_prompt())

