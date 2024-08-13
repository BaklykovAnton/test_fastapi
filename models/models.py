from sqlalchemy import MetaData, Integer, TIMESTAMP, ForeignKey, Table, Column, String, Text
from datetime import datetime

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False),
    Column('registred_at', TIMESTAMP, default=datetime.utcnow)
)

programs = Table(
    "programs",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('file_name', String, nullable=False),
    Column('text', Text, nullable=False),
    Column('user_id', Integer, ForeignKey("users.id")),
)