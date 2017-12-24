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
# In the container run
```uwsgi --http :8000 --wsgi-file wsgi.py```
to test the uwsgi application
