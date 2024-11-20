#!/bin/bash
set -ex

apt install bind9 -y
systemctl start bind9
cat <<EOF > /etc/bind/named.conf.options
options {
    directory "/var/cache/bind";
    forwarders {
        8.8.8.8;
    };
    dnssec-validation no;

    auth-nxdomain no;
    listen-on-v6 { any; };
};
EOF
cat <<EOF > /etc/bind/db.myservers.net
\$TTL 86400
@       IN      SOA     ns1.myservers.net. admin.myservers.net. (
                        2022010201      ; Serial
                        86400           ; Refresh
                        7200            ; Retry
                        604800          ; Expire
                        86400           ; Minimum TTL
                        )

@       IN      NS      ns1.myservers.net.


dansdogservice       IN      A       192.168.1.2
ns1                  IN      A       192.168.1.2
EOF

cat <<EOF > /etc/bind/named.conf.local
zone "myservers.net" {
    type master;
    file "/etc/bind/db.myservers.net";
};
EOF
systemctl restart bind9
