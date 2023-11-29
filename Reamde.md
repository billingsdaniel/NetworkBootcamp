### running vagrant vbox
1. `mkdir vagrant_test`
2. `cd vagrant_test`
3. `vagrant init "gusztavvargadr/ubuntu-desktop"`
4. `vagrant up`

#### move to system user if required. else use `sudo` before every system level command
system user do switch user (no user specified switches to root?)
`sudo su`

### how to assign static IP address

1. move to netplan directory using cd (change directory) <-- use tab key
2. `cd /etc/netplan`
3. use ls (list) to find the correct .yml file. usually something like  01-netcfg.yaml or 50-cloud-init.yaml:
4. open the file using vi. In this case, `01-cetcfg.yaml` <-- use tab key
5. `vi /etc/netplan/01-cetcfg.yaml`
6. highly advised to make a copy of the file with .bak incase you need to change it back. use `cp SOURCE DEST`
7. `cp /etc/netplan/01-cetcfg.yaml /etc/netplan/01-cetcfg.yaml.bak`
8. inside, modify the yaml code for the address(s) you want. for example
```network:
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
9. save using  write and quit
10. `:wq`
11. apply netplan
12. `netplan apply`
13. double check ip
14. `ifconfig`


#### for turning off adapters and back on
1. `ip link set eth(insert adapter#) up`
2. `ip link set eth(insert adapter#) down`
3. `ip route show`

### dhcp
1. installing dhcp server
2. `sudo apt install isc-dhcp-server`
3. change netplan to dhcp settings. dont forget backup
```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
      dhcp4: true
```

### how to change ip address of assigned MAC address
1. find MAC address of destination ${Mac Address}
2. `vi /etc/dhcp/dhcpd.conf`
3. change text to come variation of 
```
host Accountant {
hardware ethernet ${Mac Address};
fixed-address ${IP Address};
}
```
4. restart DHCP protocol
`systemctl restart isc-dhcp-server.service`
5. example
```
host Accountant {
hardware ethernet 08:00:27:02:db:1a;
fixed-address 192.168.2.100;
```
6. lease file directory
7. `/var/lib/dhcp/dhcpd.leases`
8. actually release an address in ubuntu, like for real this time,
9. `sudo systemctl restart systemd-networkd`



### ip forwarding with DHCP
1. Check the current IP forwarding status
2. `sysctl net.ipv4.ip_forward`
3. Enable IP forwarding (if not already enabled)
4. `sysctl -w net.ipv4.ip_forward=1`

## basic network troubleshooting
1. ping the gateway
2. ping the DNS servers
3. try dns lookup
4. curl google.com

### IP tables and routing
1. packet engine IP tables, a spreadsheet of rules
2. check iptables (firewall) rules:
3. review your iptables rules to ensure that they are not blocking the forwarding of packets. Use the following command to display the current rules:
4. `iptables -L`
5. If needed, you can add rules to allow forwarding. For example:
6. `iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT`
7. Replace eth0 and eth1 with your specific network interfaces.
8. Routing table
9. Double check routing tables.  Make sure there is a valid route for the destination of the packets you are trying to forward.
10. `ip route`
11. 

### Network interface configurations:
1. Double-check the configurations of the network interfaces on your router. Ensure that the interfaces are up and configured with the correct IP addresses and subnet masks.
2. `ip addr show`
3. check firewall on the destination device:
4. Check if the destination device has a firewall that might be blocking incoming packets from the router. Make sure the firewall on the destination device allows traffic from the router.

### Packet forwarding and NAT:
- If your router is performing Network Address Translation (NAT), ensure that it is correctly configured. Check the rules related to NAT in iptables.
### Logs:
1. Inspect system logs for any error messages or warnings related to networking. The logs are usually located in /var/log/, and common log files include syslog, messages, or kern.log.
2. use `| grep` to search if needed
- `tail -f /var/log/syslog`
3. Testing connectivity:
4. Use tools like ping or traceroute to test connectivity between different network segments. This can help you identify where the packet forwarding issue might be occurring.
- `ping -c 4 destination_ip`
- `traceroute destination_ip`



- enable NAT (network address translation) to allow forwarding to virtual machines
- `iptables -t nat -s 192.168.1.0/24 -A POSTROUTING -j MASQUERADE`



StefanScherer/windows_2019 --box-version 2021.05.15

## Misc commands for bash
- to delete contents of ${filename}
- `sudo cat /dev/null > ${filename}`
- how to search for correct file - 
- `systemctl status | grep ${filena`
- in git click Terminal at bottom to edit commit messages in vi only before push
- `git commit --amend`

### windows vbox
- StefanScherer/windows_2019 --box-version 2021.05.15