## Docker build project
```
docker build -t django-api .

docker run --name django-container --restart=always -p 3456:8000 -d django-api:latest

```

## Add Bat/sh file prject
```
set -ex  # -e зупиняє скрипт при помилці, -x покаже хід виконання

# ==== API ====
cd django-api/post-api
docker build -t django-api .
docker tag django-api:latest avalentyn/django-api:latest
docker push avalentyn/django-api:latest

echo "Done ---api---!"

```