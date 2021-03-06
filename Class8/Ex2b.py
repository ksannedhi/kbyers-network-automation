'''2a. Create a Python module named jnpr_devices.py. This Python module should contain a dictionary named "srx2".
This "srx2" dictionary should contain all of the key-value pairs needed to establish a PyEZ connection. You should use getpass() for the password handling.
You should import this "srx2" device definition for all of the remaining exercises in class8.

2b. Create a Python program that creates a PyEZ Device connection to "srx2" (using the previously created Python module).
Using this PyEZ connection and the RouteTable and ArpTable views retrieve the routing table and the arp table for srx2.

This program should have four separate functions:
1. check_connected() - Verify that your NETCONF connection is working. You can use the .connected attribute to check the status of this connection.
2. gather_routes() - Return the routing table from the device.
3. gather_arp_table() - Return the ARP table from the device.
4. print_output() - A function that takes the Juniper PyEZ Device object, the routing table, and the ARP table and then prints out the:
hostname, NETCONF port, username, routing table, ARP table

This program should be structured such that all of the four functions could be reused in other class8 exercises.'''

from jnpr_devices import srx1
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from pprint import pprint

srx1_connect = Device(**srx1)
srx1_connect.open()

def check_connected():
    return srx1_connect.connected

def gather_routes():
    routes = RouteTable(srx1_connect)
    routes.get()
    return routes.items()

def gather_arp_table():
    arp_entries = ArpTable(srx1_connect)
    arp_entries.get()
    return arp_entries.items()

def print_output():
    print(f'Hostname of the device: {srx1_connect.hostname}')
    print(f'NETCONF port: {srx1_connect.port}')
    print(f'NETCONF username: {srx1_connect.user}')
    if check_connected():
        print(f"Device {srx1_connect.hostname} is connected!")
    print()
    print("Routing table:")
    pprint(gather_routes())
    print()
    print("ARP table:")
    pprint(gather_arp_table())
    print()

print_output()
