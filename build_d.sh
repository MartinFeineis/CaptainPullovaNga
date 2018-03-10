#!/bin/bash

zip -r app.zip CPN/* nginx.conf uwsgi.ini requirements.txt orch.sh supervisord.conf
sudo docker build --iidfile=image.id .
rm -f cont.id
sudo docker run -d -i -p 8090:80 --cidfile=cont.id -t $(cat image.id) supervisord
#sudo docker run -i --cidfile=cont.id  -p 8090:80 -t $(cat image.id) /bin/bash