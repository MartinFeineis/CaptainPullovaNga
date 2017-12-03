FROM ubuntu:latest
WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install -y build-essential python-dev nginx python3 python3-pip
COPY requirements.txt ./
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY app.zip ./

