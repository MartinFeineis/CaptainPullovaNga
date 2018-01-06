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
sudo docker build .
sudo docker run -d -i -p 8090:80 -t 31f3fb124ebe nginx -g 'daemon off;'
sudo docker run -i -t 4a514154296a /bin/bash
```
s
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
