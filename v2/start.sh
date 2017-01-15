#!/bin/bash

docker stop v2_login_1
docker stop v2_login_db_1
docker stop v2_catalog_1
docker stop v2_player_1
docker stop v2_catalog_db_1
docker stop v2_session_db_1
docker stop nserv


docker rm v2_login_1
docker rm v2_login_db_1
docker rm v2_catalog_1
docker rm v2_player_1
docker rm v2_catalog_db_1
docker rm v2_session_db_1
docker rm nserv

docker run -d -p 1935:1935 --name nserv -v $PWD/NginxVideo-master/mp4:/var/mp4s -v $PWD/NginxVideo-master/www:/var/www nvid /usr/local/nginx-streaming/sbin/nginx

docker-compose build
docker-compose up -d

sudo docker exec v2_login_db_1 mongoimport \
--db login \
--collection users \
--drop \
--file /home/usr_test.json

sudo docker exec v2_catalog_db_1 mongoimport \
--db myflix \
--collection videos \
--drop \
--file /home/videos.json

sudo docker exec v2_catalog_db_1 mongoimport \
--db myflix \
--collection categories \
--drop \
--file /home/categories.json