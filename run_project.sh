#!/bin/bash

source env/bin/activate
python3 bot.py &
python3 manage.py runserver &

wait