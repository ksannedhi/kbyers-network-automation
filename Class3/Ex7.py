'''You have the following BGP configuration from a Cisco IOS-XR router:
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out

From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as. Return a list of tuples. 
The tuples should be (neighbor_ip, remote_as). Print your data-structure to standard output.

Your output should look similar to the following. Use ciscoconfparse to accomplish this.
​BGP Peers: 
[('10.220.88.20', '42'), ('10.220.88.32', '43')]'''

from ciscoconfparse import CiscoConfParse

bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

bgp_obj = CiscoConfParse(bgp_config.splitlines())
bgp_neigh_list = bgp_obj.find_objects(r"^\sneighbor")

neigh_list = []

for bgp_neigh in bgp_neigh_list:
    _, neigh_ip  = bgp_neigh.text.split()
    remote_as_obj_list = bgp_neigh.re_search_children(r"^\s+remote-as")
    _, remote_as = remote_as_obj_list[0].text.split()
    neigh_list.append((neigh_ip, remote_as))

print("BGP Peers:")
print(neigh_list)

