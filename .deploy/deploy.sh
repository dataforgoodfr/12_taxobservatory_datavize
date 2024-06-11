
#!/bin/sh

# Navigate to the project directory
project_dir=$(pwd)
venv_dir=$project_dir/.venv

# Warning to ensure you are at the root of the project
read -p "Please ensure $project_dir IS THE ROOT OF THE REPO before proceeding. Continue? (y/n): " answer
case ${answer:0:1} in
    y|Y )
        echo "Proceeding with the script..."
    ;;
    * )
        echo "Exiting the script..."
        exit
    ;;
esac


# Check if the virtual environment exists in the project directory
if [ ! -d "$venv_dir" ]; then
    echo "Virtual environment not found in project directory!"
    exit
fi

deploy_dir=$project_dir/.deploy/.gi-generated
mkdir -p $deploy_dir &2> /dev/null


# Update the package lists for upgrades and new package installations
sudo apt update -y
# Ensure libssl-dev is installed
sudo apt install libssl-dev

# Check if nginx is installed, if not then install it
if ! command -v nginx &> /dev/null
then
    sudo apt install -y nginx
fi

. $venv_dir/bin/activate
# Install uwsgi and gevent using pip
pip install uwsgi gevent 
# not recommended: asyncio greenlet
deactivate

# Remove existing uwsgi link if it exists and create a new one
sudo rm -f /usr/bin/uwsgi 
sudo ln -s $venv_dir/bin/uwsgi /usr/bin/uwsgi

# Generate a Systemd file for uWSGI
echo """
[Unit]
Description=Taxplorer UWSGI Server
After=syslog.target

[Service]
ExecStart=uwsgi --master --http :5000 --gevent 1000 --http-websockets --module main:web_app --logto /tmp/taxplorer.log
WorkingDirectory=$(pwd)/app
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all
User=$(whoami)

[Install]
WantedBy=multi-user.target
""" > $deploy_dir/uwsgi/taxplorer.uwsgi.service

# Move the Systemd file to the correct directory
sudo cp $deploy_dir/uwsgi/taxplorer.uwsgi.service /etc/systemd/system/taxplorer.uwsgi.service
sudo systemctl daemon-reload

# Start the uWSGI service
sudo systemctl restart taxplorer.uwsgi.service

# Enable the uWSGI service to start on boot
sudo systemctl enable taxplorer.uwsgi.service

# Create a self-signed SSL certificate
#sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/certs/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt
sudo openssl req -x509 -newkey rsa:4096 -keyout /etc/ssl/certs/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -sha256 -days 3650 -nodes -subj "/CN=localhost"
# Update the Nginx configuration to expose the application
echo """
server {
    listen 80;
    listen 443 ssl;

    server_name localhost;

    # SECURITY HEADERS
    add_header 'X-Frame-Options' 'SAMEORIGIN';
    add_header 'X-XSS-Protection' '1; mode=block';
    add_header 'X-Content-Type-Options' 'nosniff';
    add_header 'Referrer-Policy' 'same-origin';
    add_header 'Strict-Transport-Security' 'max-age=63072000';

    ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
    ssl_certificate_key /etc/ssl/certs/nginx-selfsigned.key;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host \$host;
        proxy_set_header X-Forwarded-Host \$host;

    }

}""" | sudo tee $deploy_dir/nginx/sites-available/taxplorer


if [ -f "/etc/nginx/sites-enabled/taxplorer" ]; then
  sudo mv /etc/nginx/sites-enabled/taxplorer /etc/nginx/sites-available/taxplorer.bak
fi
sudo cp $deploy_dir/nginx/sites-available/taxplorer /etc/nginx/sites-enabled/taxplorer

# Restart Nginx to apply the changes
sudo systemctl restart nginx
