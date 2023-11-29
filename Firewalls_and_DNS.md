## DNS 
-  DNS allows websites to be called by name, and not ip address, eg. google.com not 8.8.8.8
- DNS in unix uses nginx
- `apt-get update`
- `apt-get install nginx`
- uses the nginx command `sudo nginx OPPERATION`
- pronounced nginx (engine x)

### DNS using Bind

- `sudo vi /etc/bind/named.conf.options`
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
- zone file for chosen domain ${domain name}
- `sudo nano /etc/bind/db.myservers.net`
- sudo vi /etc/bind/named.conf.local
```
zone "myservers.net" {
    type master;
    file "/etc/bind/db.myservers.net";
};
```
- to restart bind
- `sudo systemctl restart bind9`


### firewall in unix uses ufw 
`
ufw status
ufw enable`