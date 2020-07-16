from Ex1_devices import my_devices
from Ex2_functions import open_napalm_connection, create_backup
from pprint import pprint

for dev_dict in my_devices:
    dev_dict_copy = dev_dict.copy()
    device_type = dev_dict_copy.pop("device_type")

    device = open_napalm_connection(dev_dict)

    print(f"ARP table for device on plaform {device_type}:")
    print("=" * 56)
    pprint(device.get_arp_table())
    print("=" * 56)
 
    print(f"NTP peers of device on plaform {device_type}:")
    print("=" * 56)
    try:
        pprint(device.get_ntp_peers())
    except NotImplementedError:
        print(f"Looks like get_ntp_peers support is not available on {device_type}.")
    print("=" * 56)

    if create_backup(device):
        print(f"Backup successfully created for {device.hostname}")
        print("=" * 56)

