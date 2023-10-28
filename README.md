# Simple django & mongodb project for ESS management


### Installation in your local environment

- Create a virtualenv
```bash
virtualenv venv --python=python3.10
```

- Start the virtualenv
```bash
source venv/bin/activate
```

- Create a `.env` to customize env settings

- Install dependencies
```bash
make install
```

- Run migrations

```bash
make migrate
```

- Create a superuser `python manage.py createsuperuser`

### Start the server

- from root directory:
```bash
make run
```

### API Documentation
- `Redoc`: http://localhost:8000/api/schema/redoc/
- `Swagger`: http://localhost:8000/api/schema/swagger-ui/

### Run linter
...TODO

### Run tests
...TODO
