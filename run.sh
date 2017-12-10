#!/usr/bin/env bash

export APP_SETTINGS=devopstools.config.DevelopmentConfig
export DATABASE_URL=postgres://postgres:postgres@localhost:5432/users_dev
export DATABASE_TEST_URL=postgres://postgres:postgres@localhost:5432/users_test

python manage.py recreate_db
python manage.py seed_db
if [[ $1 == 'test' ]]; then
    python manage.py test
    python manage.py cov
fi
python manage.py runserver -p 5555
