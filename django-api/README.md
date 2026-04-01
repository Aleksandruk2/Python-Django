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

## Working City
```
py manage.py startapp cities
python -m pip install Pillow
py manage.py makemigrations cities
py manage.py migrate

```

## Додаю superuser
```
py manage.py createsuperuser
username - admin
password - 123456
py manage.py runserver 9581

```

## Working users Custom Django
```
py manage.py startapp users
 
py manage.py makemigrations users
py manage.py migrate

```
