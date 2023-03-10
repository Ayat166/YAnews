#!/bin/bash

# Build the project
echo "Building the project..."
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
python3 pip install pygame --pre


echo "Make Migration..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear