# Трекер полезных привычек

## Описание проекта

Трекер полезных привычек — REST API-приложение на Django REST Framework для создания и отслеживания полезных и приятных привычек.

## Возможности

- Регистрация и авторизация пользователей.
- Создание, просмотр, редактирование и удаление привычек.
- Просмотр публичных привычек.
- Проверка правил создания привычек.
- Пагинация списка привычек.
- Подключение Telegram для получения напоминаний.
- Автоматическая отправка уведомлений с помощью Celery.
- Документация API через Swagger и ReDoc.

## Используемые технологии

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- Celery
- Redis
- Telegram Bot API
- drf-spectacular

## Установка и запуск

1. Клонировать репозиторий.
2. Установить зависимости с помощью Poetry:

   `poetry install`

3. Создать файл `.env` на основе `.env.template` и заполнить необходимые переменные.
4. Выполнить миграции:

   `python manage.py migrate`

5. Запустить сервер:

   `python manage.py runserver`

## Запуск Celery

Запустить Celery Worker:

`celery -A config worker -l info -P solo`

Запустить Celery Beat:

`celery -A config beat -l info`

## Документация API

- Swagger: `/api/docs/`
- ReDoc: `/api/redoc/`
- Схема API: `/api/schema/`
