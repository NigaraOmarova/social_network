from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'orm',
    user = 'nigara',
    password = '909095',
    host = 'localhost',
    port = 5432
)
