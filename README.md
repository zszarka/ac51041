# ac51041
run nginx video server
docker run -d -p 1935:1935 -p 80:80 --name nserv -v $PWD/mp4:/var/mp4s -v $PWD/www:/var/www nvid /usr/local/nginx-streaming/sbin/nginx



run php server:
docker run -d -p 80:80 --name apa -v $PWD/html-data:/var/www/html php:7.0-apache


neo4j
git clone https://github.com/Ortee/neo4j-docker-express-api.git neo4j-docker-express

cd neo4j-docker-express
sudo apt install npm
docker-compose up


mongo

start
docker run -d --name mongodb -v /home/data:/data/db -v /home/import:/home mongo:3.0

seed database
sudo docker  exec  mongodb mongoimport --db myflix --collection categories --drop --file /home/categories.jso


Restheart
sudo docker run -d -p 8080:8080 --name restheart --link mongodb:mongodb softinstigate/restheart


