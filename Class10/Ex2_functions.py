from netmiko import ConnectHandler

def ssh_command(dev_dict, cmd):
    device = ConnectHandler(**dev_dict)
    output = device.send_command(cmd)
    print(output)
    device.disconnect()

def ssh_command2(dev_dict, cmd):
    device = ConnectHandler(**dev_dict)
    output = device.send_command(cmd)
    return output
    device.disconnect()

