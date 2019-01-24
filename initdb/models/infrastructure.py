from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cells(Base):
    __tablename__ = "cells"
    __table_args__ = {"schema": "infrastructure"}
    ts = Column(DateTime, primary_key=True)
    msisdn = Column(String, primary_key=True)
    val = Column(Integer)


class Sites(Base):
    __tablename__ = "sites"
    __table_args__ = {"schema": "infrastructure"}
    ts = Column(DateTime, primary_key=True)
    msisdn = Column(String, primary_key=True)
    val = Column(Integer)
