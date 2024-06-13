# Taxplorer website for CbCR data visualization

The repository contains the source code for the
[https://www.taxplorer.eu](https://www.taxplorer.eu) Taxplorer website for
Country-By-Country Report data visualization. 

It has been developed during the 12th season of [dataforgood](https://dataforgood.fr/).

The website is deployed on
[https://www.taxplorer.eu](https://www.taxplorer.eu/). The `main` branch is the
one deployed on the production website .

The `dev` branch is deployed on the developpement website [https://dev.taxplorer.eu](https://dev.taxplorer.eu)

# Contributing

If you want to contribute a new feature, please fork the `ðev` branch and
propose a pull request. Once accepted, it will integrate the `dev` branch and
eventually be deployed on the production website once a release is created by
syncing the `main` branch with the `dev` branch.

# Local development environment

## Environment installation

TBD

## Pre-commit

To run the pre-commit, follow the instructions on how to [install pre-commit](https://pre-commit.com/) and then run them with :

    pre-commit run --all-files

The pre-commit must be run before proposing a pull request, otherwise the CI/CD
will complain about your proposed feature.

## Deployment

We deploy two websites. One for production and one for development. In both
cases, the process is the same, the only difference being the branch being used
to run the server.

Deploying a website involves : 

- cloning the repository and setting up the virtual environment,
- wrapping the start/stop of the taipy server with a systemd service
- configuring nginx with a base setup listening on port 80 and then adding https
  support with a SSL certificate

### Cloning and virtual environment

First clone the repository :

```
cd /opt/d4g
git clone https://github.com/dataforgoodfr/12_taxobservatory_dataviz.git
cd 12_taxobservatory_dataviz
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

### Systemd service file for running taipy

For easily managing the start/stop of the taipy server, we define a service
file. We actually define two service files `taxplorer.uwsgi.service` for the
production site and `taxplorer-dev.uwsgi.service` for the development website.

**File /etc/systemd/system/taxplorer.uwsgi.service**

```
[Unit]
Description=D4G Taxplorer website for CbCR visualization
After=syslog.target

[Service]
ExecStart=/opt/d4g/12_taxobservatory_dataviz/.venv/bin/uwsgi --http 127.0.0.1:5000 --gevent 1000 --http-websockets --module app.main:web_app --logto /opt/d4g/12_taxobservatory_dataviz/taxplorer.log
WorkingDirectory=/opt/d4g/12_taxobservatory_dataviz/
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all
User=d4gtaxobs

[Install]
WantedBy=multi-user.target
```

**File /etc/systemd/system/taxplorer-dev.uwsgi.service**

```
[Unit]
Description=D4G Taxplorer website for CbCR visualization
After=syslog.target

[Service]
ExecStart=/opt/d4g/12_taxobservatory_dataviz_dev/.venv/bin/uwsgi --http 127.0.0.1:5001 --gevent 1000 --http-websockets --module app.main:web_app --logto /opt/d4g/12_taxobservatory_dataviz/taxplorer.log
WorkingDirectory=/opt/d4g/12_taxobservatory_dataviz_dev/
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all
User=d4gtaxobs

[Install]
WantedBy=multi-user.target
```

Once these service files are defined, we enable and start them :

```
sudo systemctl enable taxplorer.uwsgi.service
sudo service taxplorer.uwsgi start

sudo systemctl enable taxplorer-dev.uwsgi.service
sudo service taxplorer-dev.uwsgi start
```

Now, you should have your servers up and running. To ensure this is the case,
you must be able to contact the machine with your browser at
`http://localhost:5000` and `http://localhost:5001`. The `localhost` here refers
to the server name. To access it from a remote machine, you can add a ssh tunnel
before connecting with your browser :

```
ssh -L 5000:localhost:5000  YOUR_LOGIN@THE_IP_OF_THE_MACHINE
```

If accessing the taipy server from your browser fails, you have an issue. To
debug the issue, you can:
- check the logs of the service : `sudo service taxplorer.uwsgi status` and in
  the log file `tail /opt/d4g/12_taxobservatory_dataviz/taxplorer.log`
- stop the service and run the `uwsgi` command manually :

```
# For debugging issues
sudo service taxplorer.uwsgi stop
cd /opt/d4g/12_taxobservatory_dataviz/
/opt/d4g/12_taxobservatory_dataviz/.venv/bin/uwsgi --http 127.0.0.1:5000 --gevent 1000 --http-websockets --module app.main:web_app --logto /opt/d4g/12_taxobservatory_dataviz/taxplorer.log

```

And pay particular attention to python errors.

### Nginx setup

#### Basic configuration with http support

For nginx, you can remove the default website :

```
cd /etc/nginx/sites-enabled
sudo rm -rf default
```

Then add your website definition. The basic definition is almost the same
whether you deploy the production or development website. In the template file
below, you must replace the two variables `MY_SERVER_NAME` and `MY_PORT` as :

- `MY_SERVER_NAME` with `www.taxplorer.eu` and `MY_PORT` with `5000` for the
  production website,
- `MY_SERVER_NAME` with `dev.taxplorer.eu` and `MY_PORT` with `5001` for the
  development website,

If you want to define both the production and development website, you can just
consecutively define both.

**File /etc/nginx/sites-enabled/d4g-dataviz** :
```
server {
	listen 80;
    server_name MY_SERVER_NAME;
    add_header 'X-Frame-Options' 'SAMEORIGIN';
    add_header 'X-XSS-Protection' '1; mode=block';
    add_header 'X-Content-Type-Options' 'nosniff';
    add_header 'Referrer-Policy' 'same-origin';
    add_header 'Strict-Transport-Security' 'max-age=63072000';
    ssl_certificate /etc/letsencrypt/live/www.taxplorer.eu/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.taxplorer.eu/privkey.pem;
    location / {
        proxy_pass http://127.0.0.1:MY_PORT;
        #proxy_redirect off;
        #keepalive_requests 100;
        #proxy_read_timeout 75s;
        #proxy_connect_timeout 75s;
        #proxy_http_version 1.1;
        #client_max_body_size 100M;
        #proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        #proxy_set_header X-Forwarded-Proto $scheme;
        #proxy_set_header X-Real-IP $remote_addr;
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
the server with `ip addr` and then going to `http://IP_OF_THE_SERVER`.

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
`/etc/nginx/sites-enabled/d4g-dataviz` file to 1) redirect any connection to
port `80` to port `443` and adds the definition for using the certificate. For
example, below is the definition for the development website :

```
server {
    server_name dev.taxplorer.eu;

    # SECURITY HEADERS
    add_header 'X-Frame-Options' 'SAMEORIGIN';
    add_header 'X-XSS-Protection' '1; mode=block';
    add_header 'X-Content-Type-Options' 'nosniff';
    add_header 'Referrer-Policy' 'same-origin';
    add_header 'Strict-Transport-Security' 'max-age=63072000';

    location / {
        proxy_pass http://localhost:5001;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-Host $http_host;   
    }


    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/dev.taxplorer.eu/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/dev.taxplorer.eu/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

server {
    if ($host = dev.taxplorer.eu) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    server_name dev.taxplorer.eu;
    listen 80;
    return 404; # managed by Certbot
}

```




