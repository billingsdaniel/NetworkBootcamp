#!/bin/bash
set -ex
apt-get update
sysctl -w net.ipv4.ip_forward=1

file="/etc/sysctl.conf"
line_to_add="net.ipv4.ip_forward = 1"
# Check if the line exists (but not necessarily with the correct value)
if grep -q "^net.ipv4.ip_forward" "$file"; then
    # If the line exists, update it to ensure it is set to 1
    sudo sed -i 's/^net\.ipv4\.ip_forward.*/net.ipv4.ip_forward = 1/' "$file"
    echo "Line updated in the file."
else
    echo "$line_to_add" | sudo tee -a "$file"
    echo "Line added to the file."
fi
sysctl -p

# apt install iptables-persistent -y
# iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
# iptables -t nat -s 192.168.1.0/24 -A POSTROUTING -j MASQUERADE
# sh -c 'iptables-save > /etc/iptables/rules.v4