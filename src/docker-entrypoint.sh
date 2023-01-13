#!/usr/bin/env bash
set -e
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
echo "hello kitchen, we are in! APP_HOME:$APP_HOME"
echo "SCRIPT_DIR >> $SCRIPT_DIR"


echo
echo "$@"
echo

#while ! nc -z db 3306 ; do
#    echo "Waiting for the DB Server"
#    sleep 3
#done

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
uwsgi --ini $APP_HOME/uwsgi.ini

exec "$@"
