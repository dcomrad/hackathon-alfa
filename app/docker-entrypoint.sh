#!/bin/bash

set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for postgres to start..."
  sleep 1
done
echo "Postgres started"

alembic upgrade head
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornH11Worker --bind 0.0.0.0:$FASTAPI_PORT
