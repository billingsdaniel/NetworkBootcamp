### running vagrant vbox
1. `mkdir vagrant_test`
2. `cd vagrant_test`
3. `vagrant init "gusztavvargadr/ubuntu-desktop"`
4. `vagrant up`

#### move to system user if required. else use `sudo` before every system level command
system user do switch user (no user specified switches to root?)\
`sudo su`

### how to assign static IP address

1. move to netplan directory using cd (change directory) <-- use tab key\
    `cd /etc/netplan`
2. use ls (list) to find the correct .yml file. usually something like  01-netcfg.yaml or 50-cloud-init.yaml:
3. open the file using vi. In this case, `01-netcfg.yaml` <-- use tab key\
`vi /etc/netplan/01-netcfg.yaml`
4. highly advised to make a copy of the file with .bak incase you need to change it back. use `cp SOURCE DEST`\
`cp /etc/netplan/01-netcfg.yaml /etc/netplan/01-netcfg.yaml.bak`
5. inside, modify the yaml code for the address(s) you want. for example
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
6. save using  write and quit\
`:wq`
7. apply netplan\
 `netplan apply`
8. double check ip\
`ifconfig`


#### for turning off adapters and back on
`ip link set eth(insert adapter#) up`\
`ip link set eth(insert adapter#) down`\
`ip route show`

### dhcp
1. installing dhcp server\
`sudo apt install isc-dhcp-server`
2. change netplan on client machine to use dhcp. dont forget backup
    ```
    network:
      version: 2
      renderer: networkd
      ethernets:
        enp3s0:
          dhcp4: true
    ```

### how to create dhcp reservation (mac address to ip)
1. find MAC address of host ${Mac Address}\
`ip a`
2. open dhcp config
`vi /etc/dhcp/dhcpd.conf`
3. change config text to 
    ```
    host Accountant {
    hardware ethernet ${Mac Address};
    fixed-address ${IP Address};
    }
    ```
4. restart DHCP 
`systemctl restart isc-dhcp-server.service`
5. example
    ```
    host Accountant {
    hardware ethernet 08:00:27:02:db:1a;
    fixed-address 192.168.2.100;
    ```
6. lease file directory\
 `/var/lib/dhcp/dhcpd.leases`
- to actually release an address in ubuntu, client side \
`sudo systemctl restart systemd-networkd`


## basic network troubleshooting
- ping the gateway
- ping the DNS servers
- try dns lookup
- curl google.com

## iptables and routing
### ip forwarding with router
- Check the current IP forwarding status\
 `sysctl net.ipv4.ip_forward`
- Enable IP forwarding (if not already enabled)\
 `sysctl -w net.ipv4.ip_forward=1`
###  iptables
1. packet engine IP tables, a spreadsheet of rules
2. check iptables (firewall) rules:
3. review your iptables rules to ensure that they are not blocking the forwarding of packets. Use the following command to display the current rules:\
`iptables -L`
4. If needed, you can add rules to allow forwarding. For example:\
`iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT`
5. Replace eth0 and eth1 with your specific network interfaces.
6. Double check routing tables.  Make sure there is a valid route for the destination of the packets you are trying to forward.\
`ip route`
7. enable NAT (network address translation) to allow forwarding to virtual machines\
`iptables -t nat -s 192.168.1.0/24 -A POSTROUTING -j MASQUERADE`


### Network interface configurations:
1. Double-check the configurations of the network interfaces on your router. Ensure that the interfaces are up and configured with the correct IP addresses and subnet masks.\
`ip addr show`
2. check firewall on the destination device:
3. Check if the destination device has a firewall that might be blocking incoming packets from the router. Make sure the firewall on the destination device allows traffic from the router.

### Packet forwarding and NAT:
- If your router is performing Network Address Translation (NAT), ensure that it is correctly configured. Check the rules related to NAT in iptables.
### Logs:
1. Inspect system logs for any error messages or warnings related to networking. The logs are usually located in /var/log/, and common log files include syslog, messages, or kern.log.
2. use `| grep` to search if needed\
3. use tail command (for long log files, only displays last 10 lines)
`tail -f /var/log/syslog`\
`tail -f /var/log/syslog | grep `
4. use head command if tail doesnt display what you want, or use full log file with `| grep|`
`head -f /var/log/syslog | grep `\
`journalctl | grep `
5. Testing connectivity:
6. Use tools like ping or traceroute to test connectivity between different network segments. This can help you identify where the packet forwarding issue might be occurring.\
`ping -c 4 destination_ip`\
`traceroute destination_ip`


   
## Misc commands for bash
- to delete contents of ${filename}\
`sudo cat /dev/null > ${filename}`
- how to search for correct file - \
`systemctl status | grep ${filena`
- in git click Terminal at bottom to edit commit messages in vi only before push\
`git commit --amend`

#### windows vbox
- StefanScherer/windows_2019 --box-version 2021.05.15