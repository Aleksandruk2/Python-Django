#!/bin/bash
set -ex  # -e зупиняє скрипт при помилці, -x покаже хід виконання

# ==== WEB ====
# cd my-transfer-ts/transfer-front
# docker build -t transfer-react --build-arg VITE_API_BASE_URL=https://av-transfer.itstep.click .
# docker tag transfer-react:latest avalentyn/transfer-react:latest
# docker push avalentyn/transfer-react:latest
# echo "Done ---client---!"

# ==== API ====
cd django-api/post-api
docker build -t django-api .
docker tag django-api:latest avalentyn/django-api:latest
docker push avalentyn/django-api:latest

echo "Done ---api---!"

#read -p "Press any key to exit..."