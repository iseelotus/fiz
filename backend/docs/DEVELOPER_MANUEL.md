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


#### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.