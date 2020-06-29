from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

xe_dict = {"host": "cisco3.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_xe"}
xe_connect = ConnectHandler(**xe_dict)

param_list = ['no ip name-s', 'no ip domain-loo', 'ip name-s 1.1.1.1', 'ip name-s 1.0.0.1', 'ip domain-lookup']
op = xe_connect.send_config_set(param_list)
st_time1 = datetime.now()
op += xe_connect.send_command("ping google.com", strip_command = False, strip_prompt = False)
end_time1 = datetime.now()
print(op)
print(f"Total time taken without fast_cli {end_time1 - st_time1}")

xe_connect.disconnect()

print("*" * 80)

xe_dict2 = {"host": "cisco3.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_xe", "fast_cli": True}
xe_connect2 = ConnectHandler(**xe_dict2)

param_list2 = ['no ip name-s', 'no ip domain-loo', 'ip name-s 1.1.1.1', 'ip name-s 1.0.0.1', 'ip domain-lookup']
op2 = xe_connect2.send_config_set(param_list2)
st_time2 = datetime.now()
op2 += xe_connect2.send_command("ping google.com", strip_command = False, strip_prompt = False)
end_time2 = datetime.now()
print(op2)
print(f"Total time taken with fast_cli {end_time2 - st_time2}")

xe_connect2.disconnect()

