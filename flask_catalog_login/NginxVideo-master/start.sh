#!/bin/bash

docker stop nserv
docker rm nserv
docker build .
docker run -d -p 1935:1935 -p 80:80 --name nserv -v $PWD/mp4:/var/mp4s -v $PWD/www:/var/www nvid /usr/local/nginx-streaming/sbin/nginx
docker start nserv
