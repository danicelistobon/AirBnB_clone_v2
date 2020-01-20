#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "/server_name _;/a location /hbnb_static/ {\nalias /data/web_static/current/;\nautoindex off;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
