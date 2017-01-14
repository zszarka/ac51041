docker stop session_web_1
docker stop session_db_1

docker rm session_web_1
docker rm session_db_1

docker-compose build
docker-compose up