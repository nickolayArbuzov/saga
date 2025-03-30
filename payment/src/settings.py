from pydantic_settings import BaseSettings


class Database(BaseSettings):
    ASYNC_DATABASE_URL: str
    SYNC_DATABASE_URL: str

    @property
    def async_database_url(self) -> str:
        return self.ASYNC_DATABASE_URL

    @property
    def sync_database_url(self) -> str:
        return self.SYNC_DATABASE_URL

    class Config:
        env_file = ".env"
        extra = "ignore"


database_connection = Database()
