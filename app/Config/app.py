from pydantic import Field
from .base import BaseConfig, APP_PATH


class AppConfig(BaseConfig):

    PATH: str = APP_PATH
    APP_NAME: str = Field('Fastio', env='APP_NAME')
    APP_ENV: str = Field(..., env='APP_ENV')
    APP_KEY: str = Field(..., env='APP_KEY')
    APP_DEBUG: bool = Field(..., env='APP_DEBUG')
    APP_URL: str = Field(..., env='APP_URL')


AppConf = AppConfig()
