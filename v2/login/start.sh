#!/bin/bash

docker stop login_web_1
docker stop login_db_1

docker rm login_web_1
docker rm login_db_1

docker-compose build
docker-compose up

sudo docker exec login_db_1 mongoimport \
--db login \
--collection users \
--drop \
--file /home/usr_test.json