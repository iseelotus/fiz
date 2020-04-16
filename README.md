# fiz Backend

fiz is a tool for personal finance. You can book your expenditure and income, as well as switch between accounts.

# For the Reviewers

Heroku endpoint: https://fsnd-fiz.herokuapp.com/

## Roles

### Analyser

Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImU2ckxjczlkcE94TUxZOHV2ZVpPaCJ9.eyJpc3MiOiJodHRwczovL2Rldi04ZXpzMHRjZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5NWY0ZTU1M2RmYTAwYzE5ZjgwMWYyIiwiYXVkIjoiZml6IiwiaWF0IjoxNTg3MDQ1MDE2LCJleHAiOjE1ODcxMzE0MTYsImF6cCI6Im9nNTdqanIzOHZBY1d2cFZ6enVjcVQxdXNMem9rejBhIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6aXRlbXMiLCJnZXQ6aXRlbXMtYnktY2F0ZWdvcnkiXX0.OOIHA4F2dTP0BI8-BOCFbtTC3sm6h9YtKD9J1-tHs6pNx8TG9aw3MzIBJL-KSsYDwsG1JH7NUHwngHLeU_tCAAK0y1meji_WQv6iLdGHjBATHXuAPWNDm3bEjuV6sRDTO_mhJxjtoiV0jt6MtlSJ3TFJGC9vbSsJIZd9Y-62QPMxYW2JXfQcCNuW3ZWiaTVl0U7mzSP_p6dg9CDu8FGixH3krk0EkJtHNpIOHU6fFnCJWfPrDOo3tKHoTqkbUS1h7Wnpig7C0ICzMvozG_rbGsQwGzH-7mNltJ6IvQaksKEredbwe8bM3MYCWqmky72Gmm7wxHipAHo3iOk4P4EyuQ

- Analyser can view all items and items by category.


### Data Owner

Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImU2ckxjczlkcE94TUxZOHV2ZVpPaCJ9.eyJpc3MiOiJodHRwczovL2Rldi04ZXpzMHRjZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5NWY3NGZkNDMwYWUwYzA3YzNmZTNjIiwiYXVkIjoiZml6IiwiaWF0IjoxNTg3MDQ0OTU4LCJleHAiOjE1ODcxMzEzNTgsImF6cCI6Im9nNTdqanIzOHZBY1d2cFZ6enVjcVQxdXNMem9rejBhIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6aXRlbXMiLCJnZXQ6aXRlbXMiLCJnZXQ6aXRlbXMtYnktY2F0ZWdvcnkiLCJwYXRjaDppdGVtcyIsInBvc3Q6aXRlbXMiXX0.kPy8zbvXy0exN0XcKtf382uOw8_JwwbW-OuiBecjjVngMHmK8MJ3s6loGD7kNWjgTt2hTlB1vBxBWpOr4eN4LVdECRlIIDmTnqXopjcca-tsPrVNQGuXAt3cBbkA0zt2ZYEAe1Lyd2kScTHZ553JJQo1UVaMmnOu2tF8jLZjk_DQKyOeoN-GjVZAO_i92SXh1p_coSvAnwA8BeTuVjlFA6uR8qX7BzU1b2lQNchOjYH-gP1MUgFtTq7Z-bHnea4RnWRoLivHkaAQJm3d4MAC7PPLgOo0AQnu7XWbOXUbWLhk8GTa41CHjliPybiZLvidfKLzS4UfwgmWH9OEL-X6_A

- Data owner has all permissions a Analyser has.

- Data owner can delete, patch, post items

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

