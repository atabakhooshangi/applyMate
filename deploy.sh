#!/bin/bash

# Exit the script on any error
set -e

# Collect static files
python3.12 manage.py collectstatic --noinput
