from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    # Backend
    django_secret_key: str
    django_debug: bool = False
    email_host_user: str
    email_host_password: str

    # Database
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    # RabbitMQ
    rabbitmq_default_user: str
    rabbitmq_default_pass: str
    rabbitmq_host: str
    rabbitmq_port: int

    # Redis
    redis_host: str
    redis_port: int
    redis_db: int

    @property
    def celery_broker_url(self) -> str:
        return (
            f'amqp://'
            f'{self.rabbitmq_default_user}:'
            f'{self.rabbitmq_default_pass}@'
            f'{self.rabbitmq_host}:'
            f'{self.rabbitmq_port}'
        )

    @property
    def celery_result_backend(self) -> str:
        return f'redis://{self.redis_host}:{self.redis_port}/{self.redis_db}'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


env_config: EnvConfig = EnvConfig()
