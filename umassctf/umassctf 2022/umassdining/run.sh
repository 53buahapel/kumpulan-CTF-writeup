cd src
python3 -m gunicorn -w 4 --bind 0.0.0.0:8000 main:app
