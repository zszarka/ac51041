#!/bin/bash

docker stop login_web_1
docker stop login_db_1

docker rm login_web_1
docker rm login_db_1