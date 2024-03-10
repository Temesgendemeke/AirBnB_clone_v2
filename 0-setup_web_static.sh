#!/usr/bin/env bash
#web servers for the deployment of web_static

apt-get update
apt-get -y install nginx

mkdir -p /data/ /data/web_static/ /data/web_static/releases/ 
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

echo '
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
' > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/releases/test/

chown -hR ubuntu:ubuntu /data/
sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

systemctl restart nginx
