#!/bin/bash -e

set -e

# run test of this project

export IMAGE="musicscience37/pipenv:$1-test"
docker build -t "$IMAGE" "$1"
docker compose up
docker compose down
