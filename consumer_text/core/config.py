
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # mongodb configuration
    DATABASE_URL: str = 'mongodb'
    MONGO_INITDB_DATABASE: str = 'pizza_orders' 
    COLLECTION_NAME: str = 'orders'

    # redis configuration
    REDIS_HOST: str = 'redis'
    class Config:
        env_file = './.env'


settings = Settings()
