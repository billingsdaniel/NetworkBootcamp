### dhcp
1. installing dhcp server on host machine\
`sudo apt install isc-dhcp-server`
2. configure DHCP range in config
`vi /etc/dhcp/dhcpd.conf`\
```
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.2 192.168.1.100;
    option routers 192.168.1.1;
    option domain-name-servers 8.8.8.8, 8.8.4.4;
}
```
3. restart dhcp
`sudo systemctl restart isc-dhcp-server
`
4. always double check
`sudo systemctl status isc-dhcp-server
`
5. 
2. change netplan on client machine to use dhcp. dont forget backup
    ```
    network:
      version: 2
      renderer: networkd
      ethernets:
        eth0:
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

x