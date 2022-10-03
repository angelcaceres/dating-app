#!/bin/bash
ls /home/dating-app
pip3 install -r /home/dating-app/requirements.txt
python3 /home/dating-app/manage.py migrate
python3 /home/dating-app/manage.py runserver