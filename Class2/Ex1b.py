from netmiko import ConnectHandler
from getpass import getpass

xe_dict = {"host": "cisco4.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_xe"}

xe_connect = ConnectHandler(**xe_dict)

output = xe_connect.find_prompt()
output += xe_connect.send_command("ping", expect_string = r"Protocol", strip_command = False, strip_prompt = False)
output += xe_connect.send_command("\n", expect_string = r"IP", strip_command = False, strip_prompt = False)
output += xe_connect.send_command("8.8.8.8", expect_string = r"count", strip_command = False, strip_prompt = False)
output += xe_connect.send_command("\n", expect_string = r"Datagram size", strip_command = False, strip_prompt = False)
output += xe_connect.send_command("\n", expect_string = r"seconds", strip_command = False, strip_prompt = False)
output += xe_connect.send_command("\n", expect_string = r"Exten", strip_command = False, strip_prompt = False)
output += xe_connect.send_command("\n", expect_string = r"range", strip_command = False, strip_prompt = False)
output += xe_connect.send_command("\n", expect_string = r"#", strip_command = False, strip_prompt = False)

xe_connect.disconnect()
print(output)

