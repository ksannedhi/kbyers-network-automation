'''Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.
ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup
Experiment with fast_cli=True to see how long the script takes to execute (with and without this option enabled).
Verify DNS lookups on the router are now working by executing 'ping google.com'. Verify from this that you receive a ping response back.'''

from netmiko import ConnectHandler
from getpass import getpass

cisco3_dict = {"host": "cisco3.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_ios", "fast_cli": True}
cisco3_connect = ConnectHandler(**cisco3_dict)

cmd_list = ["no ip name-server", "ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]

op_fastcli = cisco3_connect.send_config_set(cmd_list)
print(op_fastcli)

print(cisco3_connect.find_prompt(), end = '')
op_ping = cisco3_connect.send_command("ping google.com", strip_prompt = False, strip_command = False) #Instead of using a separate output for ping, you can continue with the above output using +=. This will avoid additional router prompt display in the output.
print(op_ping)

