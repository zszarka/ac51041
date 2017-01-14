#!/bin/bash

docker stop catalog_web_1
docker stop catalog_db_1

docker rm catalog_web_1
docker rm catalog_db_1

docker-compose build
docker-compose up -d

sudo docker exec catalog_db_1 mongoimport \
--db myflix \
--collection videos \
--drop \
--file /home/videos.json

sudo docker exec catalog_db_1 mongoimport \
--db myflix \
--collection categories \
--drop \
--file /home/categories.json