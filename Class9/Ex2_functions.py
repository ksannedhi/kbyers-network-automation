from napalm import get_network_driver

def open_napalm_connection(dev_dict):
    device_type = dev_dict.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**dev_dict)
    device.open()
    return device

def create_backup(device):
    backup = device.get_config()
    filename = device.hostname + "-config.txt"
    with open(filename, "w") as f:
        f.write(backup["running"])
    return True

def create_checkpoint(device):
    filename = f"{device.hostname}-checkpoint.txt"
    backup = device.get_checkpoint_file()
    with open(filename, "w") as f:
        f.write(backup)
