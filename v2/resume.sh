#!/bin/bash

docker run -d -p 1935:1935 --name nserv -v $PWD/NginxVideo-master/mp4:/var/mp4s -v $PWD/NginxVideo-master/www:/var/www nvid /usr/local/nginx-streaming/sbin/nginx

docker-compose up -d