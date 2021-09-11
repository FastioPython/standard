
import os
from pathlib import Path    # Python 3.6+ only
from pydantic import BaseSettings

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
APP_PATH = "{0}".format(Path(CURRENT_DIR).parent)
ENV_PATH = "{0}/.env".format(APP_PATH)
STORAGE_PATH = "{0}/Storage".format(APP_PATH)


class BaseConfig(BaseSettings):

    class Config:
        case_sensitive = True
        env_file = ENV_PATH
        env_file_encoding = 'utf-8'
