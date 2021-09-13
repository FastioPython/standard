import os
import unittest
from unittest import mock
from app.Config.database import DatabaseConfig

fake_os_environ = {
    "DB_CONNECTION": "FakeMySQL",
    "DB_HOST": "example.com",
    "DB_PORT": "80",
    "DB_USER": "myuser",
    "DB_PASSWORD": "mypassword",
    "DB_DATABASE": "mydatabase",
}


# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict
@mock.patch.dict(os.environ, fake_os_environ, clear=True)
class TestDatabaseConf(unittest.TestCase):

    def test_app_config_from_environment(self):
        DatabaseConf = DatabaseConfig()

        self.assertEqual("FakeMySQL", DatabaseConf.DB_CONNECTION)
        self.assertEqual("example.com", DatabaseConf.DB_HOST)
        self.assertEqual(80, DatabaseConf.DB_PORT)
        self.assertEqual("myuser", DatabaseConf.DB_USER)
        self.assertEqual("mypassword", DatabaseConf.DB_PASSWORD)
        self.assertEqual("mydatabase", DatabaseConf.DB_DATABASE)
