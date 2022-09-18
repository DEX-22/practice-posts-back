from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta,engine

user = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=true),
    Column("name", String(255)),
    Column("user_name", String(255)),
    Column("password", String(255)),
)

meta.create_all(engine)
