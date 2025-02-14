### Описание:

API платформы для обучения на Django REST Framework.

### Стек:

- DRF
- PostgreSQL
- Celery
- Rabbitmq
- Redis
- Docker

### Запуск:

1. #### Создать файл `.env` по примеру `.env.example`:

   *Для отправки email нужно создать "Пароль для внешнего приложения".*

   *Пример для mail.ru: <https://help.mail.ru/mail/mailer/password/>*

   *Вписываем в `.env`:*

    - `EMAIL_HOST_USER` *- Ваша почта*

    - `EMAIL_HOST_PASSWORD` *- пароль для внешнего приложения.*

2. #### Запустить:

```shell
docker compose up --build
```
