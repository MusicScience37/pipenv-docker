#!/bin/bash -e

# run test of this project

compose_file=pipenv/docker-compose.test.yml
docker-compose -f $compose_file up --build
docker-compose -f $compose_file down
