## Database

### PostgreSQL

To start a postgres server:

```$ pg_ctl -D /usr/local/var/postgres start```

To create a new database:

```createdb <database_name>```

### Migrate

We use flask-migrate for the database migration management. 

To initiate the migration:

```$ flask db init```

To generate an  migration:

```$ flask db migrate -m "Migration message"```

Then you can check the generated migration, especially the `upgrade()` method. Change if needed. If everything seems fine, you can apply the migration to the database:

```$ flask db upgrade```

To rollback the database migration, use:

```$ flask db downgrade```

## Authorization

### Auth0

Auth0 is used for third party authorization.

To log in:

```
https://dev-8ezs0tce.eu.auth0.com/authorize?
    audience=fiz&
    response_type=token&
    client_id=og57jjr38vAcWvpVzzucqT1usLzokz0a&
    redirect_uri=http://localhost:5000/login-callback

```

To log out:

```
https://dev-8ezs0tce.eu.auth0.com/v2/logout?
  client_id=og57jjr38vAcWvpVzzucqT1usLzokz0a
```


#### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.