#!/bin/sh
mkdir -p /run/nginx
mkdir -p /var/log/supervisor
apk add --update
apk add --no-cache python3 zip supervisor nginx python3-dev gcc make postgresql-dev musl-dev libxml2-dev libxslt-dev g++ gcc-avr linux-headers
pip3 install --upgrade pip
pip3 install cython
pip3 install --no-build-isolation --no-cache-dir -r requirements.txt
cp nginx.conf /etc/nginx/nginx.conf
cp supervisord.conf /etc/supervisord.conf
#update-rc.d nginx enable
#service nginx start
cd /var/www/CPN
#uwsgi --socket :8000 --wsgi-file CPN/wsgi.py