from pydantic import Field
from .base import BaseConfig, APP_PATH, ENV_PATH


class DatabaseConfig(BaseConfig):

    DEFAULT_DRIVER = 'mysql'
    DB_CONNECTION: str = Field(..., env='DB_CONNECTION')
    DB_HOST: str = Field('127.0.0.1', env='DB_HOST')
    DB_PORT: int = Field(..., env='DB_PORT')
    DB_USER: str = Field(..., env='DB_USER')
    DB_PASSWORD: str = Field(..., env='DB_PASSWORD')
    DB_DATABASE: str = Field('', env='DB_DATABASE')
    DB_PREFIX: str = Field('', env='DB_PREFIX')


DatabaseConf = DatabaseConfig()