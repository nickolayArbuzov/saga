from pydantic_settings import BaseSettings


class Database(BaseSettings):
    DATABASE_URL: str

    @property
    def database_url(self) -> str:
        return self.DATABASE_URL

    class Config:
        env_file = ".env"
        extra = "ignore"


database_connection = Database()
