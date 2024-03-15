# Web Hosting Basics

## Contents
1. Using nginx
2. Generating Certs

## Using nginx
Nginx is a tool used to host websites. 
1. Install nginx (pronounced engine x)
    ```
    apt-get update
    apt-get install nginx
    ```
2. Start nginx\
`systemctl start nginx`

## Generate Certs
To generate cert self-signed for dansdogerservice.myservers.net with openssl. MAKE SURE YOU ARE NOT IN THE HTML DIRECTORY BEFORE GENERATING CERT KEYS. This is a security issue. You don't want to issue the key in the same directory as the website going to clients.
1. Move to secure directory \
`cd /etc/nginx/ssl/`
2. Generate private key: \
`openssl genpkey -algorithm RSA -out dansdogservice.key`
3. request cert signing \
`openssl req -new -key dansdogservice.key -out dansdogservice.csr`
4. MAKE SURE COMMON NAME MATCHES dansdogervice.myservers.net
5. Gen self signed cert
   ```
   openssl x509 \
     -req \
     -days 365 \
     -in dansdogservice.csr \
     -signkey dansdogservice.key \
     -out dansdogservice.crt
   ```
6. You can modify `-days` to say how long cert is issued for
7. Double check cert \
`openssl x509 -in dansdogservice.crt -text -noout`
8. Make sure private key isn't hosted anywhere (like /var/www/html), as it is sensitive info for security of the hosted site
9. You can set permissions for restricting file access with `chmod` \
`chmod 400 dansdogservice.key`
10. If self signing the cert, it will trigger a security warning in the browser because the cert is not signed by a Cert Authority. Best to only use self signed certs for testing. In prod, you would likely use a viable trusted cert from a CA company or a cert assigned project wide.
11. Modify config for nginx \
`vi /etc/nginx/sites-enabled/default`
12. Example tls config
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
13. Restart nginx\
`systemtcl restart nginx`
14. Double check nginx status\
`systemctl status nginx`
15. Double check if website is functional with above cert in browser
