#!/usr/bin/env bash
set -e
# SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
CURRENT_PATH=$(pwd)
echo "Hello $APP_HOME, we are in! APP_HOME: $APP_HOME"
echo "CURRENT_PATH >> $CURRENT_PATH"


echo
echo "$@"
echo

#while ! nc -z db 3306 ; do
#    echo "Waiting for the DB Server"
#    sleep 3
#done

exec "$@"
