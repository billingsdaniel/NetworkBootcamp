## Linux Networking Basics
This is how to set up networking on a new machine, how to forward network traffic, and firewall basics in linux.

## Contents
1. Using Sudo
2. Network Adapters
3. Assigning Static IP
4. Iptables and Routing
   1. Traffic Forwarding
   2. Basic Network Troubleshooting
   3. Logs
5. Firewall
6. Basic Network Troubleshooting

### Using Sudo
When using system level commands, sometimes it is required to have admin privileges to affect the system as a whole and not just the specific user you are logged in as. In cases like this, you use `sudo` before a command. For example:
`sudo apt-get install nginx` 
You can also switch to a superuser if you want ALL commands to run this way. Doing so may have some drawbacks by making any mistakes have larger than desired impact, and harder to fix afterwards.
`sudo su`

### Network Adapters
For turning on or off hardware adapters (physical or otherwise):
`ip link set eth(insert adapter#) up`\
`ip link set eth(insert adapter#) down`\
To check if the adapter is on the route table:
`ip route show`

### Assigning Static IP address:
Sometimes you want to assign a static IP address to a machine for a specific purpose instead of allowing DHCP to handle assignment. This may be because you need other machines to allways have a specific reference point, such as being used as a router or DNS server. 
In linux, static IP is handled by the netplan folder, and using `vi` to edit reference files.
1. move to netplan directory using cd (change directory) <-- use tab key\
    `cd /etc/netplan`
2. use ls (list) to find the correct .yml file. usually something like  01-netcfg.yaml or 50-cloud-init.yaml:
3. open the file using vi. In this case, `01-netcfg.yaml` <-- use tab key\
`vi /etc/netplan/01-netcfg.yaml`
4. highly advised to make a copy of the file with .bak incase you need to change it back. use `cp SOURCE DEST`\
`cp /etc/netplan/01-netcfg.yaml /etc/netplan/01-netcfg.yaml.bak`
5. inside, modify the yaml code for the address(s) you want. for example
    ```
   network:
      version: 2
      renderer: networkd
      ethernets:
        eth0:
          addresses:
            - 192.168.1.1/24
    ``` 
6. save using  write and quit\
`:wq`
7. apply netplan\
 `netplan apply`
8. double check ip\
`ifconfig`


   

## Iptables and Routing
When connecting two networks, it is necessary to forward packets through specific connection points, in this case a machine set up as a router. To do this we must set up ip forwarding. This may be used to connect an internal network to another machine connected to the internet or to connect multiple subnets together. This is a good place to use `sudo`, and having a static IP is usually required. IP Tables is a packet engine, a spreadsheet of rules for the network to follow. We also make use of MASQUERADE to connect our private network to the internet. MASQUERADE translates this traffic, mapping the packets to the correct location on the network. This is also known as NAT (Network Address Translation)
### Step 1: Sysctl
- Check the current IP forwarding status\
 `sysctl net.ipv4.ip_forward`
- Enable IP forwarding (if not already enabled)\
 `sysctl -w net.ipv4.ip_forward=1`
- Save these settings to config file to provide continuity of service across reboots
- `vi /etc/sysctl.conf`
```
net.ipv4.ip_forward = 1
```
- apply changes with
```
sysctl -p
```
### Step 2: iptables
1. packet engine IP tables, a spreadsheet of rules
2. check iptables (firewall) rules:
3. review your iptables rules to ensure that they are not blocking the forwarding of packets. Use the following command to display the current rules:\
`iptables -L`
4. If needed, you can add rules to allow forwarding. For example:\
5. install iptables-persistent
`apt install iptables-persistent`
6. apply iptables configs
`iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT`
7. Replace eth0 and eth1 with your specific network interfaces.
8. Double check routing tables.  Make sure there is a valid route for the destination of the packets you are trying to forward.\
`ip route`
9. enable NAT (network address translation) to allow forwarding to virtual machines\
`iptables -t nat -s 192.168.1.0/24 -A POSTROUTING -j MASQUERADE`
10. save iptables config
`sh -c 'iptables-save > /etc/iptables/rules.v4`

### Step 3: Network interface configurations:
1. Double-check the configurations of the network interfaces on your router. Ensure that the interfaces are up and configured with the correct IP addresses and subnet masks.\
`ip addr show`
2. check firewall on the destination device:
3. Check if the destination device has a firewall that might be blocking incoming packets from the router. Make sure the firewall on the destination device allows traffic from the router.

### Step 4: Packet forwarding and NAT:
- If your router is performing Network Address Translation (NAT), ensure that it is correctly configured. Check the rules related to NAT in iptables.

## Logs:
1. Inspect system logs for any error messages or warnings related to networking. The logs are usually located in /var/log/, and common log files include syslog, messages, or kern.log.
2. use `| grep` to search if needed\
3. use tail command (for long log files, only displays last 10 lines)
`tail -f /var/log/syslog`\
`tail -f /var/log/syslog | grep `
4. Use head command if tail doesn't display what you want, or use the full log file with `| grep|`
`head -f /var/log/syslog | grep `\
`journalctl | grep `
5. Testing connectivity:
6. Use tools like ping or traceroute to test connectivity between different network segments. This can help you identify where the packet forwarding issue might be occurring.\
`ping -c 4 destination_ip`\
`traceroute destination_ip`



## Firewall
The basic firewall system in linux is `ufw`, Uncomplicated Firewall. Sometimes this may cause issues when connecting. You can enable or disable this when needed, or check status, but try to not get in the habit of leaving it off.
`ufw status`\
`ufw enable`


## Basic Network Troubleshooting
- ping the gateway
- ping the DNS servers
- try dns lookup
- curl google.com
