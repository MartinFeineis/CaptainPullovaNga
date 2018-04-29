FROM alpine:latest
WORKDIR /var/www/
RUN apk update
COPY app.zip ./
RUN unzip app.zip

# Install debug tools 
RUN apk add curl vim

RUN chmod +x entrypoint.sh
RUN ./entrypoint.sh
EXPOSE 80
