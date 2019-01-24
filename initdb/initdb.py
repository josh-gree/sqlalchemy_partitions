
import os

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.declarative import declarative_base


from events import Calls, Sms, Topup, Mds
from infrastructure import Cells, Sites

Base = declarative_base()
tables = [Calls, Sms, Topup, Mds]
schemas = ["events"]

con_str = "postgres://{}@:5432/{}".format(
    os.environ["POSTGRES_USER"], os.environ["POSTGRES_DB"]
)
engine = create_engine(con_str, echo=True)
Session = sessionmaker(bind=engine)

# create schemas
schemas = ["events", "infrastructure", "geography", "cache", "etl"]
[engine.execute(CreateSchema(schema)) for schema in schemas]

# create tables
events_tables = [Calls, Sms, Topup, Mds]
infrastructure_tables = [Cells, Sites]

all_tables = events_tables + infrastructure_tables

Base.metadata.create_all(engine, tables=[table.__table__ for table in all_tables])
