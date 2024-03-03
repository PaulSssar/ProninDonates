python manage.py migrate

python manage.py collectstatic --clear --noinput

gunicorn donates.wsgi:application --bind 0.0.0.0:8000
