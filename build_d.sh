#!/bin/bash

zip -r app.zip CPN/* nginx.conf uwsgi.ini emperor.uwsgi.service requirements.txt orch.sh
sudo docker build --iidfile=image.id .
rm -f cont.id
sudo docker run -d -i -p 8090:80 -t $(cat image.id) nginx -g 'daemon off;' --cidfile=cont.id
#sudo docker run -i --cidfile=cont.id  -p 8090:80 -t $(cat image.id) /bin/bash