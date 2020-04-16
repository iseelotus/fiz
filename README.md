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
$ pipenv shell
$ export FLASK_APP=api.py
$ flask run --reload
```

### Running the Tests

To run the tests:

```
$ pipenv shell
$ python test-app.py
```

### Testing

To run the tests:

```bash
python test_app.py
```

## REST Endpoints

### /items

#### GET

Get items.

Response example:

```
{
    "items": [
        {
            "amount": "2800.25",
            "category_id": 3,
            "date": "Fri, 31 Jan 2020 00:00:00 GMT",
            "description": "salary",
            "expense": false,
            "id": 1
        },
        {
            "amount": "16.99",
            "category_id": 1,
            "date": "Fri, 31 Jan 2020 00:00:00 GMT",
            "description": "Aldi",
            "expense": true,
            "id": 2
        },
        {
            "amount": "8.32",
            "category_id": 1,
            "date": "Sat, 08 Feb 2020 00:00:00 GMT",
            "description": "Netto",
            "expense": true,
            "id": 3
        }
    ],
    "success": true
}
```

#### POST

Create new item.

Body example:

```
{
    "description": "florist",
    "amount": "8.99",
    "date": "20200308",
    "expense": true,
    "category_id": 4
}
```

Response example:

```
{
    "created": 9,
    "items": [
        {
            "amount": "16.5",
            "category_id": 4,
            "date": "Thu, 13 Feb 2020 00:00:00 GMT",
            "description": "Treptower Klause",
            "expense": true,
            "id": 5
        },
        {
            "amount": "8.99",
            "category_id": 4,
            "date": "Sun, 08 Mar 2020 00:00:00 GMT",
            "description": "florist",
            "expense": true,
            "id": 8
        },
        {
            "amount": "8.99",
            "category_id": 4,
            "date": "Sun, 08 Mar 2020 00:00:00 GMT",
            "description": "florist",
            "expense": true,
            "id": 9
        }
    ],
    "success": true
}
```

### /items/{item_id}

#### PATCH

Update existing item with the id **item_id**

Response example:

```
{
    "success": true
}
```

#### DELETE

Delete an existing item. If the item doesn't exist, return 404.

Response example:

```
{
    "deleted": 9,
    "success": true
}
```

### /categories/{category_id}/items

#### GET

Get all items under given category with id **category_id**.

Response example:

```
{
    "category_id": 1,
    "items": [
        {
            "amount": "16.99",
            "category_id": 1,
            "date": "Fri, 31 Jan 2020 00:00:00 GMT",
            "description": "Aldi",
            "expense": true,
            "id": 2
        },
        {
            "amount": "8.32",
            "category_id": 1,
            "date": "Sat, 08 Feb 2020 00:00:00 GMT",
            "description": "Netto",
            "expense": true,
            "id": 3
        }
    ],
    "success": true
}
```

## Roles

### Analyser

- Analyser can view all items and items by category.

### Data Owner

- Data owner has all permissions a Analyser has.

- Data owner can delete, patch, post items
