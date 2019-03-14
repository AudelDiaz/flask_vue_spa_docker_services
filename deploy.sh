#!/bin/bash
# Este script fue diseñado para ejecutarse en Ubuntu 18.04
# Autor: @audeldiaz
sudo apt update && sudo apt install docker docker-compose
sudo rm -rf app/
git clone https://github.com/AudelDiaz/flask_vue_spa_docker_services.git project
cd project
docker-compose pull
docker-compose build
docker-compose up --scale frontend=2 --scale backend=4 -d