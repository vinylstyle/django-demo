## Requirements

- Django
- Django REST Framework

## Directory Structure

- / - Django Project
- /api_todo - Todo API
- /app - Django app
- /frontend - React/Tailwind
- /website - Django Project Configurations

## Initialize migrations

Execute this command to initialize the system tables.

python manage.py makemigrations api_todo
python manage.py migrate

## Create an admin user

Execute this command to create an admin user.

python manage.py createsuperuser

## Building React/Tailwind

Go into /frontend and run these commands.

1. npm install
2. npm run build

## Running server

After installing Django, execute this command to start the server.

python manage.py runserver

## Accessing functionality

- Main Web App - http://127.0.0.1:8000
- User API - http://127.0.0.1:8000/users/
- Todo API - http://127.0.0.1:8000/todos/
-- Get Todo - http://127.0.0.1:8000/todos/<id>/
