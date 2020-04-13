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