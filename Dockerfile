FROM debian:latest
WORKDIR /usr/src/app
RUN apt-get update ; apt-get install --fix-missing
RUN apt-get install -y build-essential python-dev nginx python3 python3-pip zip 

# Install debug tools 
RUN apt-get install -y curl vim
RUN update-rc.d nginx enable
RUN service nginx start
COPY requirements.txt ./
COPY nginx.conf /etc/nginx/nginx.conf
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY app.zip ./
RUN unzip app.zip
EXPOSE 80
CMD service nginx restart && tail -f /var/log/syslog | grep nginx
