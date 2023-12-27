#!/usr/bin/env bash
# exit on error
set -o errexit

#para ejecutar requirements.txt
pip install -r requirements.txt
#para que se genere la carpeta por defecto de archivos estáticos
python manage.py collectstatic --no-input
#para ejecutar las migraciones 
python manage.py migrate
