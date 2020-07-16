from Ex1_devices import device_list
from datetime import datetime
from netmiko import ConnectHandler

start_time = datetime.now()

def sh_ver_output(dev_dict, sh_ver):
    device = ConnectHandler(**dev_dict)
   
    dev_type = dev_dict.pop("device_type")
    print(f"Printing 'show version' output for the {dev_type}:")
    
    output = device.send_command(sh_ver)
    print(output)
    device.disconnect()

sh_ver_cmd = "show version"
for device in device_list:
    sh_ver_output(device, sh_ver_cmd)

end_time = datetime.now()

total_processing_time = end_time - start_time

print("#" * 53)
print(f"This all took a total time of {total_processing_time} seconds.")
print("#" * 53)
