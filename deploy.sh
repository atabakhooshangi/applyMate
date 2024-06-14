#!/bin/bash

# Exit the script on any error
set -e
pip3 install -r requirements.txt
# Collect static files
python3.12 manage.py collectstatic --noinput
