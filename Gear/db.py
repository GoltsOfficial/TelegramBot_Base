from peewee import PostgresqlDatabase
from .config import config

db = PostgresqlDatabase(
    config.POSTGRES_DB,
    user=config.POSTGRES_USER,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    port=config.POSTGRES_PORT,
)
