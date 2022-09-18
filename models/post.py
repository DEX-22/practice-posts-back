from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String,DateTime
from config.db import meta,engine
from datetime import datetime

posts = Table(
    "posts",
    meta,
    Column("id", String(255), primary_key=True),
    Column("author", String(255)),
    Column("title", String(255)),
    Column("content", String(255)),
    Column("published", String(255)),
    Column("created_at", DateTime),
    Column("published_at", DateTime,nullable = True)
)

meta.create_all(engine)
