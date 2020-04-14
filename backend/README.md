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

### Database Setup

With Postgres running, initiate the database through SQLAlchemy Migrate.

```bash
flask db upgrade
```

### Running the Server

To run the flask server:

```bash
export FLASK_APP=api.py
flask run --reload
```

### Testing

To run the tests:

```bash
python test_app.py
```

## REST Endpoints

### /items

#### GET

#### POST

#### PATCH

#### DELETE

### /categories/{category_id}/items

#### GET

## Roles

### Analyser

* Analyser can view all items and items by category.

### Data Owner

* Data owner has all permissions a Analyser has.

* Data owner can delete, patch, post items


