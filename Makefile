#!/bin/sh

install-dev:
	docker-compose -f docker-compose.dev.yml build
	docker-compose -f docker-compose.dev.yml up -d
	sleep 4
	docker container exec library_app python manage.py makemigrations
	docker container exec library_app python manage.py migrate
	docker container exec library_app python manage.py createsuperuser --noinput

install-prod:
	docker-compose -f docker-compose.prod.yml build
	docker-compose -f docker-compose.prod.yml up -d
	sleep 4
	docker container exec library_app python manage.py migrate
	docker container exec library_app python manage.py createsuperuser --noinput

run-dev:
	docker-compose -f docker-compose.dev.yml up -d

run-prod:
	docker-compose -f docker-compose.prod.yml up -d

run-migrations:
	docker container exec library_app python manage.py makemigrations
	docker container exec library_app python manage.py migrate

stop:
	docker-compose stop

show-urls:
	docker container exec library_app python manage.py show_urls

flake8:
	@flake8 app/ --ignore D203 \
         --exclude app/library/settings.py,app/library/wsgi.py,app/library/core/migrations \
         --max-complexity 10

tests:
	docker container exec library_app pytest library/core/tests/

logs:
	docker container logs -f library_app

clear-dev:
	docker-compose -f docker-compose.dev.yml down -v

clear-prod:
	docker-compose -f docker-compose.prod.yml down -v