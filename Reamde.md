`sudo su`
`vi /etc/netplan`  #<-- tab key

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```

`netplan apply`
`ifconfig`


for turning off adapters and back on
`ip link set eth(insert adapter#) up`
`ip link set eth(insert adapter#) down`
`ip route show`

sudo apt install isc-dhcp-server


# how to set ifconfig back to dhcp
```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
      dhcp4: true
```

# how to search for correct file - systemctl status |grep ${filename}
# how to change ip address of assigned MAC address
# find MAC address of destination
`vi /etc/dhcp/dhcpd.conf`

# change text to come variation of

```
host Accountant {
hardware ethernet ${Mac Address};
fixed-address ${IP Address};
}
```
# if destination address desired is 10.0.0.101

# restart DHCP protocol

`sudo systemctl restart isc-dhcp-server.service`

host Accountant {
hardware ethernet #MAC ADDRESS#;
fixed-address #IP ADDRESS;
}
host Accountant {
hardware ethernet 08:00:27:02:db:1a;
fixed-address 192.168.2.100;


# to delete contents of ${filename}
`sudo cat /dev/null > ${filename}`

# lease file directory
`/var/lib/dhcp/dhcpd.leases`

# actually release an address in ubuntu, like for real this time,
`sudo systemctl restart systemd-networkd`

# in git click Terminal at bottom to edit commit messages in vi only before push
`git commit --amend`

# ip forwarding with DHCP
# Check the current IP forwarding status
sysctl net.ipv4.ip_forward

# Enable IP forwarding (if not already enabled)
sysctl -w net.ipv4.ip_forward=1

# basic network troubleshooting
# ping the gateway
# ping the DNS servers
# ry dns lookup
# curl google.com
#

# packet engine IP tables, a spreadsheet of rules
#Check iptables (firewall) rules:
Review your iptables rules to ensure that they are not blocking the forwarding of packets. Use the following command to display the current rules:

bash
Copy code
iptables -L
If needed, you can add rules to allow forwarding. For example:

bash
Copy code
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
Replace eth0 and eth1 with your specific network interfaces.

Routing table:
Verify that the routing table is correctly set up. You can view the routing table using the ip route command. Make sure there is a valid route for the destination of the packets you are trying to forward.

bash
Copy code
ip route
Network interface configurations:
Double-check the configurations of the network interfaces on your router. Ensure that the interfaces are up and configured with the correct IP addresses and subnet masks.

bash
Copy code
ip addr show
Firewall on the destination device:
Check if the destination device has a firewall that might be blocking incoming packets from the router. Make sure the firewall on the destination device allows traffic from the router.

Packet forwarding and NAT:
If your router is performing Network Address Translation (NAT), ensure that it is correctly configured. Check the rules related to NAT in iptables.

Logs:
Inspect system logs for any error messages or warnings related to networking. The logs are usually located in /var/log/, and common log files include syslog, messages, or kern.log.

bash
Copy code
tail -f /var/log/syslog
Testing connectivity:
Use tools like ping or traceroute to test connectivity between different network segments. This can help you identify where the packet forwarding issue might be occurring.

bash
Copy code
ping -c 4 destination_ip
traceroute destination_ip
By systematically checking these aspects, you should be able to identify and resolve the issue with packet forwarding on your Linux router. If the problem persists, you may need to provide more specific details about your network configuration for further assistance.





# enable NAT (network address translation) to allow forwarding to virtual machines
`iptables -t nat -s 192.168.1.0/24 -A POSTROUTING -j MASQUERADE`



