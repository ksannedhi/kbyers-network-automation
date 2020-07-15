'''For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'.
Save this output to a file in the current working directory.'''

from netmiko import Netmiko
from getpass import getpass

cisco_ios_xe = {"host": "cisco3.lasthop.io",
                "username": "pyclass",
                "password": getpass(),
                "device_type": "cisco_xe",
                "session_log": "show_ver.txt"}

cisco_connect = Netmiko(**cisco_ios_xe)

with open("show_ver.txt", "w") as f:
    f.write(cisco_connect.send_command("sh ver"))

cisco_connect.disconnect()
