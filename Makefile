#!/bin/sh

install-dev:
	sudo docker compose -f docker-compose.yml -f docker-compose.dev.yml build
	sudo docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d
	sleep 4
	sudo docker container exec library_app python manage.py makemigrations
	sudo docker container exec library_app python manage.py migrate
	sudo docker container exec library_app python manage.py createsuperuser --noinput

install-prod:
	sudo docker compose -f docker-compose.yml -f docker-compose.prod.yml build
	sudo docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
	sleep 4
	sudo docker container exec library_app python manage.py migrate
	sudo docker container exec library_app python manage.py createsuperuser --noinput

run-dev:
	sudo docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d

run-prod:
	sudo docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

run-migrations:
	sudo docker container exec library_app python manage.py makemigrations
	sudo docker container exec library_app python manage.py migrate

stop:
	sudo docker compose stop

show-urls:
	sudo docker container exec library_app python manage.py show_urls

flake8:
	@flake8 app/ --ignore D203 \
		 --exclude app/library/settings/,app/library/wsgi.py,app/library/core/migrations \
         --max-complexity 10

tests:
	sudo docker container exec library_app pytest -s library/

logs:
	sudo docker container logs -f library_app

clean-dev:
	sudo docker compose -f docker-compose.yml -f docker-compose.dev.yml down -v

clean-prod:
	sudo docker compose -f docker-compose.yml -f docker-compose.prod.yml down -v