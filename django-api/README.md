# Create Project
```
python --version

```

# Create venv - віртуальне серидовище для вашого проекту і пакетів
```

py -m venv .venv
або
python3 -m venv .venv

```

# Activate venv
```
cd projects\django-api

.venv\Scripts\activate.bat - win
source ./venv/bin/activate - macOs/Linux

```

# Install Django
```

python.exe -m pip install --upgrade pip
python3 -m pip install --upgrade pip

py -m pip install Django

py

>>> import django
>>> print(django.get_version())
>>> quit()

python -m django --version

mkdir post-api
django-admin startproject myapi post-api

```

## Run project
```

cd post-api
py manage.py runserver 9581

```

## Install Postgres
```
pip install psycopg2-binary
py manage.py migrate
python3 manage.py migrate

```


## Перегляд списку бібліотек
```
pip freeze
pip freeze > requirements.txt

pip install djangorestframework

```


## Додаю superuser
```
python manage.py createsuperuser
py manage.py createsuperuser
username - admin
password - 123456
py manage.py runserver 9581

```

## Working City
```
py manage.py startapp cities
py manage.py makemigrations cities
py manage.py migrate

```


## Working categories Django
```

cd atbmvt
py manage.py startapp categories
py manage.py makemigrations categories
py manage.py migrate

```


## Working products Django
```
cd atbmvt
py manage.py startapp products
py manage.py makemigrations products
py manage.py migrate
py manage.py makemigrations products
py manage.py migrate

```

## Working productImages Django
```
cd atbmvt

py manage.py makemigrations productImages
py manage.py migrate

```
