#!/bin/bash

docker run --name nginx-proxy -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock jwilder/nginx-proxy

docker run --name bilab-ssts -d -e VIRTUAL_HOST=ssts.ctf.esc escctf/bilab_ssts
docker run --name bilab-intranet -d -e VIRTUAL_HOST=intranet.ctf.esc escctf/bilab_intranet
docker run --name bilab-bot -d escctf/bilab_bot
