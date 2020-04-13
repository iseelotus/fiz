# fiz Backend

fiz is a tool for personal finance. You can book your expenditure and income, as well as switch between accounts.

## Getting Started

### Installling Dependencies

#### Python 3.8

Follow the instructions in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment & Dependencies

You should install `pipenv` on your machine.

The following command installs the dependencies:

```bash
pipenv install
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, initiate the database through SQLAlchemy Migrate.

```flask db upgrade```

