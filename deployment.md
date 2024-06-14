# Deployment

We deploy two websites. One for production and one for development. In both
cases, the process is the same, the only difference being the branch being used
to run the server.

Deploying a website involves : 

- cloning the repository and setting up the virtual environment,
- wrapping the start/stop of the taipy server with a systemd service
- configuring nginx with a base setup listening on port 80 and then adding https
  support with a SSL certificate

## Variables to be defined

For this documentation, we use generic variables you will need to adapt :

- `MY_PROD_DOMAIN` : which is the domain behind the production website
  www.somewhere.com
- `MY_PROD_PORT` : which is the port on which the production taipy will be
  listening incomnig connectiosn 
- `MY_PROD_PATH_TO_APP` : which is the path on your linux box where the
  repository is cloned for production

- `MY_DEV_DOMAIN` : which is the domain behind the development website
  dev.somewhere.com
- `MY_DEV_PORT` : which is the port on which the production taipy will be
  listening incomnig connectiosn 
- `MY_DEV_PATH_TO_APP` : which is the path on your linux box where the
  repository is cloned for production

We suppose you want to deploy the website on the machine with ip `MY_SERVER_IP`
on which you can connect with ssh using the login `MY_LOGIN`.

For deploying the production and development websites, the procedure is the
same, you just have to replace the `MY_PROD_xxx` variables by `MY_DEV_xxx`
variables.

## Cloning and virtual environment

First clone the repository :

```
git clone https://github.com/dataforgoodfr/12_taxobservatory_dataviz.git
MY_PROD_PATH_TO_APP
cd MY_PROD_PATH_TO_APP
```

If you want to deploy the development website, you must checkout the `dev`
branch. If you want to deploy the production website, you must checkout the
`main` branch. 

```
git checkout dev   # For development website
git checkout main  # For production website
```

You can then create a local virtual environment, install poetry as well as the
project dependencies :
```
. ./d4g-utils/install_poetry.sh
```

We need some extra packages for the deployment :

```
source .venv/bin/activate
pip install uwsgi gevent
```

## Systemd service file for running taipy

For easily managing the start/stop of the taipy server, we define a service
file. 

**File /etc/systemd/system/dataviz.service**

```
[Unit]
Description=Website deployment for CbCR data visualization
After=syslog.target

[Service]
ExecStart=MY_PROD_PATH_TO_APP/.venv/bin/uwsgi --http 127.0.0.1:MY_PROD_PORT --gevent 1000 --http-websockets --module app.main:web_app --logto MY_PROD_PATH_TO_APP/taxplorer.log
WorkingDirectory=MY_PROD_PATH_TO_APP
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all
User=MY_LOGIN

[Install]
WantedBy=multi-user.target
```

Once these service files are defined, we enable and start them :

```
sudo systemctl enable dataviz.service
sudo service dataviz start
```

Now, you should have your servers up and running. To ensure this is the case,
you must be able to contact the machine with your browser at
`http://localhost:MY_PROD_PORT`. The `localhost` here refers
to the server name. To access it from a remote machine, you can add a ssh tunnel
before connecting with your browser :

```
ssh -L MY_PROD_PORT:localhost:MY_PROD_PORT  MY_LOGIN@MY_SERVER_IP
```

If accessing the taipy server from your browser fails, you have an issue. To
debug the issue, you can:

- check the logs of the service : `sudo service dataviz status` and in
  the log file `tail MY_PROD_PATH_TO_APP/taxplorer.log`
- stop the service and run the `uwsgi` command manually :

```
# For debugging issues
sudo service dataviz stop

cd MY_PROD_PATH_TO_APP
MY_PROD_PATH_TO_APP/.venv/bin/uwsgi --http 127.0.0.1:MY_PROD_PORT --gevent 1000 --http-websockets --module app.main:web_app --logto MY_PROD_PATH_TO_APP/taxplorer.log

```

And pay particular attention to python errors.

## Nginx setup

### Basic configuration with http support

For nginx, you can remove the default website :

```
cd /etc/nginx/sites-enabled
sudo rm -rf default
```

Then add your website definition. If you want to define both the production and development website, you can just consecutively define both.

**File /etc/nginx/sites-enabled/dataviz** :
```
server {
	listen 80;
    server_name MY_PROD_DOMAIN;
    add_header 'X-Frame-Options' 'SAMEORIGIN';
    add_header 'X-XSS-Protection' '1; mode=block';
    add_header 'X-Content-Type-Options' 'nosniff';
    add_header 'Referrer-Policy' 'same-origin';
    add_header 'Strict-Transport-Security' 'max-age=63072000';

    location / {
        proxy_pass http://127.0.0.1:MY_PROD_PORT;
        proxy_set_header Host $http_host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
    }
}
```

You can test the definition with :

```
sudo nginx -t
```

If there is no error, you can enable and start/restart the nginx service :

```
sudo systemctl enable nginx
sudo service nginx restart
```

You should now be able to navigate to `www.taxplorer.eu`. If you do not have yet
a binding between the domain name `www.taxplorer.eu` and the IP of the server
hosting the website, you can anyway test the connection by getting the IP of
the server with `ip addr` and then going to `http://MY_SERVER_IP`.

### Adding the SSL support for https

For adding the SSL support for secured connection, we will use [certbot](https://certbot.eff.org/). For example, on a debian + nginx configuration, the steps to follow are :

```
sudo apt update && sudo apt install -y snapd
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx
```

From there, you will have to select the website for which you want to get and
install a SSL certificate. Certbot will also modify your
`/etc/nginx/sites-enabled/dataviz` file to 1) redirect any connection to
port `80` to port `443` and adds the definition for using the certificate. For
example, below is the definition for the development website :

```
server {
    server_name MY_PROD_DOMAIN;

    # SECURITY HEADERS
    add_header 'X-Frame-Options' 'SAMEORIGIN';
    add_header 'X-XSS-Protection' '1; mode=block';
    add_header 'X-Content-Type-Options' 'nosniff';
    add_header 'Referrer-Policy' 'same-origin';
    add_header 'Strict-Transport-Security' 'max-age=63072000';

    location / {
        proxy_pass http://localhost:MY_PROD_PORT;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-Host $http_host;   
    }


    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/MY_PROD_DOMAIN/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/MY_PROD_DOMAIN/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

server {
    if ($host = MY_PROD_DOMAIN) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    server_name MY_PROD_DOMAIN;
    listen 80;
    return 404; # managed by Certbot
}

```





