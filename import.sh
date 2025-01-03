#!/bin/bash

DOCKER_CONTAINER=$(docker compose ps -q)

if [ -z "$DOCKER_CONTAINER" ]; then
    echo "No running Docker container found."
    exit 1
fi

docker exec -it $DOCKER_CONTAINER bash -c 'beet import /records/import'