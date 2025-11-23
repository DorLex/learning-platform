## API платформы для обучения.

### Описание:

Тестовое задание API платформы для обучения.  
Модули: `курсы`, `уроки`.  
Привязка доступов пользователя к курсам.  
Комплексная статистика курсов.

### Стек:

- `Django REST Framework`
- `pydantic-settings`
- `PostgreSQL`
- `Celery`
- `RabbitMQ`
- `Redis`
- `Docker`

### Установка зависимостей:

1. Создать окружение через `poetry`.

2. Установить только основные зависимости, необходимые для запуска:
   ```shell
   poetry install --no-root --without dev
   ```

3. Установить все зависимости, включая `dev`/`test` (+linter, +pre-commit и т.д.):
    ```shell
    poetry install --no-root
    ```

### Pre-commit, Linter, Formatter:

- Установить `pre-commit` хуки:
    ```shell
    pre-commit install
    ```

- Ручной запуск линтера и форматера:
    ```shell
    ruff check --fix --show-fixes && ruff format
    ```

### Запуск:

1. Создать файл `.env` по примеру `example.env`.  
   *Для отправки email нужно создать "Пароль для внешнего приложения".*  
   *Пример для mail.ru: <https://help.mail.ru/mail/mailer/password/>*  
   *Вписываем в `.env`:*
    - `EMAIL_HOST_USER` *- Ваша почта*
    - `EMAIL_HOST_PASSWORD` *- пароль для внешнего приложения.*

2. Запуск в докере всего проекта:
    ```shell
    make up
    ```
3. Запуск только инфраструктуры:
    ```shell
    make infra
    ```
