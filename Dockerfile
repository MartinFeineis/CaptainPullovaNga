FROM debian:latest
WORKDIR /var/www/
RUN apt-get update ; apt-get install --fix-missing
RUN apt-get install -y zip apt-utils
COPY app.zip ./
RUN unzip app.zip

# Install debug tools 
RUN apt-get install -y curl vim
RUN useradd -ms /bin/bash newuser

RUN chmod +x orch.sh
RUN ./orch.sh
EXPOSE 8080
