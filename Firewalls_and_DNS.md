#DNS

apt-get update
apt-get install nginx


nginx 
#pronounced nginx (engine x, or gyne for memes)
# USE CHAT GPS FOR EVERYTHING!!

#DNS using Bind

`sudo vi /etc/bind/named.conf.options`

```
options {
    directory "/var/cache/bind";
    forwarders {
        8.8.8.8;
    };

    dnssec-validation auto;

    auth-nxdomain no;
    listen-on-v6 { any; };
};
```

#zone file for chosen domain ${domain name}

`sudo nano /etc/bind/db.myservers.net`

sudo nano /etc/bind/named.conf.local

zone "myservers.net" {
    type master;
    file "/etc/bind/db.myservers.net";
};

# bind restart
`sudo systemctl restart bind9`


#firewalls
`
ufw status
ufw enable`