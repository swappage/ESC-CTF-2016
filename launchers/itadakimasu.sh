#!/bin/bash


docker run --name itadakimasu-mysql \
  --env MYSQL_ROOT_PASSWORD=supersecretpasswordyolozomg \
  --env MYSQL_USER=blog --env MYSQL_PASSWORD=rotfloblog --env MYSQL_PORT=3306 --env MYSQL_DATABASE=blog \
  -d mysql:5.5

docker run --name itadakimasu \
  --link itadakimasu-mysql:mysqlserver \
  --publish 5000:5000 \
  --env MYSQL_USER=blog --env MYSQL_PASSWORD=rotfloblog --env MYSQL_PORT=3306 --env MYSQL_DATABASE=blog \
  -d escctf/itadakimasu
