#!/bin/sh

install-dev:
	sudo docker-compose -f docker-compose.dev.yml build
	sudo docker-compose -f docker-compose.dev.yml up -d
	sleep 4
	sudo docker container exec library_app python manage.py makemigrations
	sudo docker container exec library_app python manage.py migrate
	sudo docker container exec library_app python manage.py createsuperuser --noinput

install-prod:
	sudo docker-compose -f docker-compose.prod.yml build
	sudo docker-compose -f docker-compose.prod.yml up -d
	sleep 4
	sudo docker container exec library_app python manage.py migrate
	sudo docker container exec library_app python manage.py createsuperuser --noinput

run-dev:
	sudo docker-compose -f docker-compose.dev.yml up -d

run-prod:
	sudo docker-compose -f docker-compose.prod.yml up -d

run-migrations:
	sudo docker container exec library_app python manage.py makemigrations
	sudo docker container exec library_app python manage.py migrate

stop:
	sudo docker-compose stop

show-urls:
	sudo docker container exec library_app python manage.py show_urls

tests:
	sudo docker container exec library_app pytest library/core/tests.py

logs:
	sudo docker container logs -f library_app

clear-dev:
	sudo docker-compose -f docker-compose.dev.yml down -v

clear-prod:
	sudo docker-compose -f docker-compose.prod.yml down -v