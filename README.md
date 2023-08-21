# Проект "Программа самообучения"

## Краткое описание

LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы. Проект выполнен на Windows.
Создан с использованием Python и Django REST framework. Авторизация настроена с помощью JWT, настроен вывод документации
через Swagger и Redoc, реализовано асинхронное выполнение задач с помощью Celery и Schedule. В качестве брокера
используется Redis, в качестве базы данных PostgreSQL. Также в проекте имеется интеграция с сервисом платежей Stripe.

## Инструкция по запуску с Docker

1. Установить docker соответствующей ОС с официального сайта: https://docs.docker.com/
2. Создать образ:
   ```bash
   docker-compose build
   ```
3. Запустить образ:
   ```bash
   docker-compose up
   ```
   При запуске должны примениться миграции и запуститься сервер проекта.

## Инструкция по запуску без Docker

1. Создайте файл .env по образцу в файле .env.sample. 
2. Установите зависимости проекта, указанные в файле pyproject.toml.
3. Установите redis (ссылка на пакет для Windows: https://github.com/microsoftarchive/redis/releases).
4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
5. Выполните миграции

   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```

6. При необходимости загрузите тестовые данные с помощью команд или же внесите свои собственные данные.
   ```bash
   python manage.py fill_course
   python manage.py fill_lesson
   python manage.py fill_payment
   python manage.py fill_user
   ```
7. Для запуска асинхронных задач необходимо запустить Celery и Celery-beat
    ```bash
    celery -A config worker -P eventlet -l INFO 
   ```

   ```bash
    celery -A config beat -l info -S django 
   ```

## Технологии в проекте (стек)

* Python 3.11
* Django
* DRF
* PostgreSQL
* JWT
* Celery
* Redis
* Unittest
