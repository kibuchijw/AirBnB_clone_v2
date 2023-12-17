#!/usr/bin/env bash
# Update repositories and install nginx on the server
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo touch /data/web_static/releases/test/index.html
echo "Hello World!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Create or update symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure Nginx
echo '
server {
    listen 80;
    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
    }
    error_page 404 /404.html;
    location /404 {
            root /var/www/html;
            internal;
    }
}' > /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
