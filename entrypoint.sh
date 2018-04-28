#!/bin/sh
apk add --update
apk add --no-cache python3 zip supervisor nginx python-dev
pip3 install --upgrade pip
pip3 install --no-cache-dir -r requirements.txt
cp nginx.conf /etc/nginx/nginx.conf
cp supervisord.conf /etc/supervisord.conf
#update-rc.d nginx enable
#service nginx start
cd /var/www/CPN
#uwsgi --socket :8000 --wsgi-file CPN/wsgi.py