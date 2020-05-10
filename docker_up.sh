#!/usr/bin/env bash
rm -rf dist
rm -rf *.egg-info
python3 setup.py sdist
docker-compose  up --build --force-recreate