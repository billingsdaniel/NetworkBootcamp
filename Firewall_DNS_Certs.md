## testing DNS and Certs with TLS
DNS allows websites to be called by name, and not ip address, eg. google.com not 8.8.8.8


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
- zone file for chosen domain ${domain name}\
`sudo nano /etc/bind/db.myservers.net`\
`sudo vi /etc/bind/named.conf.local`\
    ```
    zone "myservers.net" {
        type master;
        file "/etc/bind/db.myservers.net";
    };
    ```
- to restart bind\
`sudo systemctl restart bind9`


### firewall in unix uses ufw (uncomplicated firewall)

`ufw status`\
`ufw enable`

### using nginx to host website
- install nginx (pronounced engine x)
    ```
    apt-get update
    apt-get install nginx
    ```

- start nginx\
`systemctl start nginx`
- other commands for systemctl
  1. start
  2. stop
  3. status
  4. restart
  5. enable 
### to generate cert self-signed for dansdogerservice.myservers.net with openssl

1. gen private key:\
`openssl genpkey -algorithm RSA -out dansdogservice.key`

1. request cert signing\
`openssl req -new -key dansdogservice.key -out dansdogservice.csr`

3. MAKE SURE COMMON NAME MATCHES dansdogervice.myservers.net

4. gen self signed cert\
`openssl x509 -req -days 365 -in dansdogservice.csr -signkey dansdogservice.key -out dansdogservice.crt`
5. can modify -days to say how long cert is leased for
6. double check cert\
`openssl x509 -in dansdogservice.crt -text -noout`
7. make sure private key isnt hosted anywhere, sensitive info for security of hosted site
8. can set permissions for restricting file access with `chmod`\
`chmod 400 dansdogservice.key`
9. If self signing certs, will trigger sec warning in browser since not signed by Cert Authority. Best to only use for testing. In prod, likely using a viable trusted cert from a CA company or project wide.
10.  modify config for nginx \
`vi /etc/nginx/sites-enabled/default`
11. example tls config
    ```
    server {
    
        listen 443 ssl;
    
        server_name dansdogservice.myservers.net;
    
    
        ssl_certificate /etc/nginx/ssl/server.crt;
    
        ssl_certificate_key /etc/nginx/ssl/private.key;
    
    
        # Other SSL configurations (optional)
    
        ssl_protocols TLSv1.2 TLSv1.3;
    
        ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384';
    
        ssl_prefer_server_ciphers off;
    
    
      
    
    }
    ```
12. restart nginx\
`systemtcl restart nginx`
13. double check nginx status\
`systemctl status nginx`
14. double check if website is functional with above cert in browser
