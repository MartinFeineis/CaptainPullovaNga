#!/bin/bash

zip -r app.zip CPN/* nginx.conf uwsgi.ini emperor.uwsgi.service requirements.txt orch.sh
sudo docker build --iidfile=image.id .
sudo docker run -d -i -p 8090:80 -t $(cat image.id) nginx -g 'daemon off;'
#sudo docker run -i -t $(cat image.id) /bin/bash