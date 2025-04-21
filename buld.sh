#!/usr/bin/env bash
# exit on error
set -o errexit

# Установка Python зависимостей
pip install -r requirements.txt

# Очистка старых статических файлов
python manage.py collectstatic --no-input --clear

# Сборка фронтенда
#cd frontend
#npm install
#npm run build
#cd ..

# Копирование собранных файлов фронтенда
# mkdir -p staticfiles
# cp -r frontend/dist/* staticfiles/

# Сборка бэкенда

python manage.py migrate

# Создание суперпользователя
python createsuperuser.py 
python manage.py collectstatic --no-input
echo staticfiles собраны