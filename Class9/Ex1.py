from napalm import get_network_driver
from Ex1_devices import my_devices
from pprint import pprint

def open_napalm_connection(dev_dict):
    dev_type = dev_dict.pop("device_type")
    driver = get_network_driver(dev_type)
    device = driver(**dev_dict)
    device.open()
    return dev_type, device

for dev_dict in my_devices:
    (device_type, device) = open_napalm_connection(dev_dict)
    print(f"For device running on {device_type} platform, below are the basic device details:")
    print("=" * 79)
    pprint(device.get_facts())
    print("=" * 79)

