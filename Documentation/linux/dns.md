## testing DNS and Certs with TLS
DNS allows websites to be called by name, and not ip address, eg. google.com not 8.8.8.8


### DNS using Bind
- Install bind
- `apt install bind9`
- Start bind
- 'systemctl start bind9'
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
- zone file for chosen domain ${domain name}\
`sudo vi /etc/bind/db.myservers.net`\
- edit zone file for domain you wish to host. this is what bind does. it connects the ip address and the hostname in a domain
```

$TTL 86400
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
```


  
`sudo vi /etc/bind/named.conf.local`\
    ```

    zone "myservers.net" {
        type master;
        file "/etc/bind/db.myservers.net";
    };
    ```
- to restart bind\
`sudo systemctl restart bind9`

