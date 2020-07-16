from ciscoconfparse import CiscoConfParse

bgp_data = """router bgp 44
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
   route-policy ALLOW out"""

bgp_data_lines = CiscoConfParse(bgp_data.splitlines())
neighbor_data = bgp_data_lines.find_objects_w_child(parentspec = r"^\s+neighbor", childspec = r"^\s+remote-as")

print("BGP Peers:")
bgp_neigh_list = []
for neighbor in neighbor_data:
    neighbor_ip = neighbor.text
    neighbor_ip = neighbor_ip.strip(" neighbor ")
    remote_as_data = neighbor.re_search_children(r"remote-as")
    remote_as = remote_as_data[0].text
    remote_as = remote_as.strip("  remote-as ")
    bgp_neigh_list.append((neighbor_ip, remote_as))

print(bgp_neigh_list)

