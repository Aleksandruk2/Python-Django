# Create Project
```

python --version

```

# Create venv - віртуальне серидовище для вашого проекту і пакетів
```

py -m venv .venv
python3 -m venv .venv

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

mkdir atbmvt
django-admin startproject mysite atbmvt


 
```

# Activate venv
```
cd projects\djangomvt

.venv\Scripts\activate.bat - win
source ./venv/bin/activate - macOs/Linux

```

## Run project
```

cd atbmvt
py manage.py runserver 9581

```

## Install Postgres
```
pip install psycopg2-binary
py manage.py migrate
python3 manage.py migrate

```

## Додаю superuser
```
python manage.py createsuperuser
py manage.py createsuperuser
username - admin
password - 123456
py manage.py runserver 9581

```

## Working users Custom Django
```
py manage.py startapp users

pip install Pillow
 
py manage.py makemigrations users

```

## Перегляд списку бібліотек, їх збереження та клонування проєкту
```
pip freeze
pip freeze > requirements.txt
git clone https://github.com/Aleksandruk2/Python-Django.git
cd Python-Django
cd djangomvt
py -m venv .venv
.venv\Scripts\activate.bat

python.exe -m pip install --upgrade pip
pip install -r requirements.txt
cd atbmvt
py manage.py runserver 9581

```

## Working categories Django
```

cd atbmvt
py manage.py startapp categories
py manage.py makemigrations categories
py manage.py migrate

```
