from pydantic import Field
from .base import BaseConfig, STORAGE_PATH


class StorageConfig(BaseConfig):

    DEFAULT_DRIVER: str = Field('local', env='STORAGE_DRIVER')
    PATH: str = STORAGE_PATH

    STORAGE_DRIVERS = {
        'local': {
            'path': STORAGE_PATH,
        },
        's3': {
            'driver': 's3',
            'key': Field(..., env='AWS_ACCESS_KEY_ID'),
            'secret': Field(..., env='AWS_SECRET_ACCESS_KEY'),
            'region': Field(..., env='AWS_DEFAULT_REGION'),
            'bucket': Field(..., env='AWS_BUCKET'),
            'url': Field(..., env='AWS_URL'),
            'endpoint': Field(..., env='AWS_ENDPOINT'),
        },
    }


StorageConf = StorageConfig()
