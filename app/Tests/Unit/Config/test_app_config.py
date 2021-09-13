import os
import unittest
from unittest import mock
from app.Config.app import AppConfig

fake_os_environ = {
    "APP_NAME": "FakeApp",
    "APP_ENV": "development",
    "APP_KEY": "fake_secret_key",
    "APP_DEBUG": "false",
    "APP_URL": "http://example.com",
}


# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict
@mock.patch.dict(os.environ, fake_os_environ, clear=True)
class TestAppConf(unittest.TestCase):

    def test_app_config_from_environment(self):
        AppConf = AppConfig()

        self.assertEqual("FakeApp", AppConf.APP_NAME)
        self.assertEqual("development", AppConf.APP_ENV)
        self.assertEqual("fake_secret_key", AppConf.APP_KEY)
        self.assertEqual("http://example.com", AppConf.APP_URL)
