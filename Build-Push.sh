#!/bin/bash
set -ex  # -e зупиняє скрипт при помилці, -x покаже хід виконання


# ==== API ====
cd django-api/post-api
docker build -t django-api .
docker tag django-api:latest avalentyn/django-api:latest
docker push avalentyn/django-api:latest

echo "Done ---api---!"

# ==== WEB ====
cd ../../my-post
docker build -t my-post --build-arg VITE_API_BASE_URL=http://localhost:4512 .
docker tag my-post:latest avalentyn/my-post:latest
docker push avalentyn/my-post:latest

echo "Done ---client---!"

#read -p "Press any key to exit..."