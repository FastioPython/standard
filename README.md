# Fastio

Full-stack python web framework based on FastAPI

## Pre-requires

- Python 3.7
- MySQLclient

To install support mysqlclient for python run this command:

```shell
sudo apt-get install python3.7-dev default-libmysqlclient-dev
```

## Development

Let follow these step to setup project.

Step 1: Create .env file

```shell
cd app
cp .env.example .env
```

Step 2: Config MySQL connection

```text
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=
DB_PASSWORD=
DB_DATABASE=
```

Step 3: Run project

```shell
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Step 4: Verify project works 

```shell
curl --location --request GET 'http://127.0.0.1:8000'
```

Result

```text
It works!
```

## Documentation

Full document to start development you can find at: [https://fastio.dev](https://fastio.dev)

## Credit

- FastAPI

## Reference

- https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
