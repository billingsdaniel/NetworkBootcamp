# Linux DNS
DNS allows websites to be called by name, and not ip address, eg. google.com not 8.8.8.8

## Contents
1. Bind
2. Troubleshooting

## DNS using Bind
1. Install bind if it isn't installed already \
   `apt install bind9`
2. Start bind9 \
   `systemctl start bind9`
3. Edit config file for bind \
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

4. Edit zone file for domain you wish to host. this is what bind does. it connects the ip address and the hostname in a domain \
   `sudo vi /etc/bind/db.myservers.net`
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
5. Edit config file for bind to direct to the zone file \
   `sudo vi /etc/bind/named.conf.local`
   ```
   zone "myservers.net" {
       type master;
       file "/etc/bind/db.myservers.net";
   };
   ```
6. Restart bind to apply settings \ 
`sudo systemctl restart bind9`

## Troubleshooting
1. You can use `nslookup` to test if the nameserver is returning domains correctly.
2. Use `systemctl status bind9` to check if bind is running.
3. If problems continue to arise, check logs with `journalctl`. You can use `-b` to only see journal for current boot, `| grep ` to search for keywords in the log, or  `-n x` to check most recent x number of entries.
