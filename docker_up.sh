#!/bin/bash
python3 setup.py sdist
docker-compose  up --build --force-recreate