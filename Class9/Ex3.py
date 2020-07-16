from Ex2_functions import open_napalm_connection
from Ex1_devices import my_devices

for dev_dict in my_devices:
    dev_dict_copy = dev_dict.copy()
    device_type = dev_dict_copy.pop("device_type")
    
    device = open_napalm_connection(dev_dict)
    
    if device_type == "ios":
        device.load_merge_candidate(filename = "Ex3_ios_loopbacks")
        print(device.compare_config())
        input("Press 'Enter' key if you are OK to apply this configuration to the ios platform.")
    else:
        device.load_merge_candidate(filename = "Ex3_eos_loopbacks")
        print(device.compare_config())
        input(f"Press 'Enter' key if you are OK to apply this configuration to the eos platform.")

    device.commit_config()
    print("Following changes are committed successfully.")

