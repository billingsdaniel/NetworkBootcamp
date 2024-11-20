#!/bin/bash
set -ex
apt-get update

sudo apt install isc-dhcp-server -y
sudo systemctl start isc-dhcp-server

sudo bash -c "cat > /etc/dhcp/dhcpd.conf <<EOF

option domain-name "example.org";
option domain-name-servers ns1.example.org, ns2.example.org;

default-lease-time 600;
max-lease-time 7200;
ddns-update-style none;

subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.2 192.168.1.100;
    option routers 192.168.1.1;
    option domain-name-servers 8.8.8.8, 8.8.4.4;
}


#### TEST
EOF"
sudo systemctl restart isc-dhcp-server
sudo systemctl restart systemd-networkd