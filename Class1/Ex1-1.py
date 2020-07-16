from netmiko import ConnectHandler

nxos1_dict = {"host": "nxos1.lasthop.io", "username": "pyclass", "password": "88newclass", "device_type": "cisco_nxos"}
nxos1_connect = ConnectHandler(**nxos1_dict)

print(nxos1_connect.find_prompt())
nxos1_connect.disconnect()

