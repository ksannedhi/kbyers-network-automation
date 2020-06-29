import yaml

def yaml_load(file_name = "Ex2a.yml"):
    with open(file_name) as f:
        devices = yaml.load(f)
    return devices

def print_arp_entries(ip_mac_list):
    for arp_entry in ip_mac_list:
        print(f'{arp_entry["address"]} --> {arp_entry["hwAddress"]}')

