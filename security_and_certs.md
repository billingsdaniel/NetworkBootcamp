
# to generate cert self-signed for dansdogerservice.myservers.net with openssl

#  gen private key:

bash

Copy code

openssl genpkey -algorithm RSA -out dansdogservice.key

# request cert signing

bash

Copy code

openssl req -new -key dansdogservice.key -out dansdogservice.csr

# MAKE SURE COMMON NAME MATCHES dansdogervice.myservers.net

# gen self signed cert
bash

Copy code

openssl x509 -req -days 365 -in dansdogservice.csr -signkey dansdogservice.key -out dansdogservice.crt

# can modify -days to say how long cert is leased for


# double check cert

bash

Copy code

openssl x509 -in dansdogservice.crt -text -noout

# make sure private key isnt hosted anywhere, sensitivie info

bash

Copy code

chmod 400 dansdogservice.key



# This way, the Common Name is set in the config file, and you won't be prompted during the CSR generation.


# Remember that self-signed certificates may trigger security warnings in browsers since they are not signed by a trusted Certificate Authority. They are suitable for development and testing purposes. In a production environment, consider obtaining a certificate from a trusted CA.


# cert nginx config


server {

    listen 443 ssl;

    server_name dansdogservice.myservers.net;


    ssl_certificate /etc/nginx/ssl/server.crt;

    ssl_certificate_key /etc/nginx/ssl/private.key;


    # Other SSL configurations (optional)

    ssl_protocols TLSv1.2 TLSv1.3;

    ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384';

    ssl_prefer_server_ciphers off;


    # Other server configurations...

}





