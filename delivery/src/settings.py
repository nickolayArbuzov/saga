from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    ASYNC_DATABASE_URL: str

    @property
    def async_database_url(self) -> str:
        return self.ASYNC_DATABASE_URL

    class Config:
        env_file = ".env"
        extra = "ignore"


class RabbitMQSettings(BaseSettings):
    RABBITMQ_URL: str

    @property
    def rabbitmq_url(self) -> str:
        return self.RABBITMQ_URL

    class Config:
        env_file = ".env"
        extra = "ignore"


database_settings = DatabaseSettings()
rabbitmq_settings = RabbitMQSettings()
