#!/bin/bash -e

# run test of this project

compose_file=$1/docker-compose.test.yml
docker-compose -f $compose_file up --build
docker-compose -f $compose_file down
