#!/bin/bash

apt-get update ; apt-get install --fix-missing
apt-get install -y build-essential python-dev nginx python3 python3-pip zip
pip3 install --upgrade pip
pip3 install --no-cache-dir -r requirements.txt
cp emperor.uwsgi.service /etc/systemd/system/emperor.uwsgi.service
cp nginx.conf /etc/nginx/nginx.conf
update-rc.d nginx enable