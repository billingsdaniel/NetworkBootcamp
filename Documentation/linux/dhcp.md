# DHCP

## Contents
1. DHCP Server
2. Client Side
3. DHCP Reservations

## DHCP Server
We will be using `isc-dhcp-server` to host dhcp in linux. This service assigns ip addresses to hosted machines.
1. Installing dhcp server on host machine \
`sudo apt install isc-dhcp-server`
2. Configure DHCP range in config \
   `vi /etc/dhcp/dhcpd.conf`
   ```
   subnet 192.168.1.0 netmask 255.255.255.0 {
       range 192.168.1.2 192.168.1.100;
       option routers 192.168.1.1;
       option domain-name-servers 8.8.8.8, 8.8.4.4;
   }
   ```
3. Restart dhcp \
`sudo systemctl restart isc-dhcp-server`
4. Always double check status \
`sudo systemctl status isc-dhcp-server`

### Client Side
Next steps involve changing settings on client machines to connect to host.

1. Make backup of netplan \
`cp /etc/netplan/01-netcfg.yaml /etc/netplan/01-netcfg.yaml.bak`
2. Edit netplan to allow dhcp4 \
`vi /etc/netplan/01-netcfg.yaml`
    ```
    network:
      version: 2
      renderer: networkd
      ethernets:
        eth0:
          dhcp4: true
    ```
   `netplan apply`
3. Double check if DHCP is working.
`ip a`



### DHCP Reservation
Sometimes you need to be sure a specific machine is assigned a specific IP address. To do this you make a DHCP Reservation. 
1. Find MAC address of machine \
`ip a`
2. Open dhcp config \
`vi /etc/dhcp/dhcpd.conf`
3. Change config text to
    ```
    host Accountant {
        hardware ethernet ${Mac Address};
        fixed-address ${IP Address};
    }
    ```
4. Restart DHCP \
`systemctl restart isc-dhcp-server.service`
5. Example \
    ```
    host Accountant {
        hardware ethernet 08:00:27:02:db:1a;
        fixed-address 192.168.2.100;
    }
    ```
6. If the IP address required is already leased out or has been recently, check the lease file directory \
 `/var/lib/dhcp/dhcpd.leases`
7. To release an address, client side, run  \
`sudo systemctl restart systemd-networkd`
