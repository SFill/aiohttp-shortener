#!/bin/bash
source ./venv/bin/activate && python setup.py sdist
docker-compose  up --build --force-recreate