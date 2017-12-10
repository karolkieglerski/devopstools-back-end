#!/usr/bin/env bash

export APP_SETTINGS=project.config.DevelopmentConfig
export DATABASE_URL=postgres://postgres:postgres@localhost:5432/users_dev
export DATABASE_TEST_URL=postgres://postgres:postgres@localhost:5432/users_test

python manage.py recreate_db
python manage.py seed_db
python manage.py test
