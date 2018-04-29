# CaptainPullovaNga
trying to predict cryptocurrency prices

get number of tweets per day
get average price per day
compare tweets from today with yesterday
compare prive from today with yesterday


# Postgres Install
```
sudo apt-get install -y postgresql postgresql-contrib pgadmin3 postgresql-client
sudo su postgres -c psql
CREATE ROLE ******** WITH LOGIN PASSWORD '*************' CREATEDB
CREATE SCHEMA IF NOT EXISTS ********** AUTHORIZATION *******;
psql -h localhost -p 5432 -U <<user>> <<database>>
```

# Using Docker
```
sudo docker build --iidfile=image.id .
sudo docker run -d -i -p 8090:80 -t $(cat image.id) nginx -g 'daemon off;' --ip=192.168.10.10
sudo docker run -i -t $(cat image.id) /bin/bash
```

This will expose nginx on the docker IP something like 172.17.0.2 or similar not on localhost

Install docker on Linux Mint 18: https://coytar.wordpress.com/2017/03/23/docker-ce-on-linux-mint-18-1/
```sudo apt-get remove docker docker-engine docker.io
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates software-properties-common curl
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88 # check if the key is there
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable"
sudo apt-get update
sudo apt-get install docker-ce```
# In the container run
```uwsgi --http :8000 --wsgi-file wsgi.py```
to test the uwsgi application

# Install MongoDB on Linux Mint
This works for Ubuntu 16.04 see: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
The regular ubuntu repository installes mongo2.6 as of writing.
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl enable mongod.service 
sudo systemctl start mongod.service 
sudo systemctl status mongod.service 
```

# Working with Django
creating new Project
```django-admin startproject <project-name>```
and creating new App
```django-admin startapp <app-name>```


```sudo docker run -it alpine:latest /bin/sh```
Time with debian:latest 1:32 min:sec with alpine 34sec



 1101  ssh 192.168.10.102
 1102  profanity 
 1103  pull_upgr 
 1104  profanity 
 1105  pull_upgr 
 1106  histroy
 1107  history 
 1108  sudo du
 1109  sudo su
 1110  profanity 
 1111  cd projects/CaptainPullovaNga/
 1112  git status 
 1113  git add entrypoint.sh 
 1114  git status 
 1115  git commit -am "switching to Alpine Linux"
 1116  git status 
 1117  git push 
 1118  htop
 1119  ./build_d.sh 
 1120  hi alpine
 1121  sudo docker run -it alpine /bin/bash
 1122  sudo docker run -it alpine \bin\bash
 1123  sudo docker run -it alpine:latest /bin/bash
 1124  sudo docker run -it alpine:latest /bin/sh
 1125  ./build_d.sh 
 1126  time ./build_d.sh 
 1127  sudo docker run -it alpine:latest /bin/sh
 1128  history
