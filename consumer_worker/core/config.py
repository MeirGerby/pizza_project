
from pydantic_settings import BaseSettings
from pydantic import EmailStr


class Settings(BaseSettings):
    DATABASE_URL: str = 'mongodb://localhost:27017/'
    MONGO_INITDB_DATABASE: str = 'pizza_orders'

    class Config:
        env_file = './.env'


settings = Settings()
