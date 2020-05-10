#!/usr/bin/env bash
set -e

while !</dev/tcp/${DB_HOST}/5432
    do sleep 1
done
shortener-db upgrade head
shortener-api