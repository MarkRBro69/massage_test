# Comments Service

Проект представляет собой API для управления комментариями, включая создание, получение и масштабируемую обработку через очередь задач и уведомления в реальном времени.

## Функциональность

- Создание комментариев с поддержкой вложенности
- Получение списка комментариев с пагинацией и сортировкой
- Авторизация JWT
- Кэширование списка комментариев Redis
- Асинхронная проверка комментариев через Celery
- Межсервисное общение Kafka
- Отправка уведомлений через WebSocket
- Асинхронное изменение размера картинки

## Технологии

- Python 3.13
- Django
- Django Rest Framework
- Django Channels
- JWT
- Redis
- Celery
- Kafka
- Docker
- AWS
- S3
- Locust

## Установка и запуск проекта

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/MarkRBro69/massage_test.git
    cd massage_test
    ```
2. Создайте и настройте `.env` по примеру `env.example`:

    ```bash
    DEBUG=
    SECRET_KEY=
   
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=
    POSTGRES_HOST=
    POSTGRES_PORT=
   
    REDIS_HOST=
    REDIS_PORT=
    ```
   
3. Запустите Docker:

    ```bash
    docker-compose up --build
    ```
   
4. Сервер доступен::

    ```bash~~~~~~~~~~~~
    http://localhost:8000
    ```
## Front

| URL             | Описание                    |
|:----------------|:----------------------------|
| ``              | Домашняя страница           |
| `/register/`    | Регистрация                 |
| `/login/`       | Логин                       |
| `/comments/`    | Просмотр комментариев       |
| `/new_comment/` | Создание нового комментария |

## Эндпоинты API

| Method | URL                 | Описание                      |
|:------|:--------------------|:------------------------------|
| POST | `/api/v1/users/`    | Создание пользователя         |
| GET | `/api/v1/comments/` | Получение списка комментариев |
| POST | `/api/v1/comments/` | Создание комментария          |
| POST | `/api/v1/token/`    | Получение JWT токена          |

## Авторизация

Для получения токена сделайте запрос на:
`/api/v1/comments/`
```
{
   "username": "",
   "password": ""
}
```

После получения JWT токена его необходимо добавлять в заголовок запроса:

```http
Authorization: Bearer <ваш_токен>