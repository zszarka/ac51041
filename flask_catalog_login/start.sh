#!/bin/bash

docker stop flaskcataloglogin_login_web_1
docker stop flaskcataloglogin_login_db_1
docker stop flaskcataloglogin_catalog_web_1
docker stop flaskcataloglogin_catalog_db_1
docker stop nserv

docker rm flaskcataloglogin_login_web_1
docker rm flaskcataloglogin_login_db_1
docker rm flaskcataloglogin_catalog_web_1
docker rm flaskcataloglogin_catalog_db_1
docker rm nserv

docker run -d -p 1935:1935 -p 80:80 --name nserv -v $PWD/NginxVideo-master/mp4:/var/mp4s -v $PWD/NginxVideo-master/www:/var/www nvid /usr/local/nginx-streaming/sbin/nginx

docker-compose build
docker-compose up

sudo docker exec flaskcataloglogin_login_db_1 mongoimport \
--db login \
--collection users \
--drop \
--file /home/usr_test.json

sudo docker exec flaskcataloglogin_catalog_db_1 mongoimport \
--db myflix \
--collection videos \
--drop \
--file /home/videos.json

sudo docker exec flaskcataloglogin_catalog_db_1 mongoimport \
--db myflix \
--collection categories \
--drop \
--file /home/categories.json