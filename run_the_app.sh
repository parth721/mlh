#!/bin/bash

#Fetch latest changes from the target branch & merge into the  PR branch
git fetch origin main
git merge origin/main

#create & activate a virtual environment (need to study this part)
python -m venv env
source env/bin/activate

#Install dependencies
pip install -r requirments.txt

#Apply database migration
python manage.py migrate

#Run tests
python manage.py test