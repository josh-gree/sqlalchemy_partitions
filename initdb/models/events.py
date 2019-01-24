from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Calls(Base):
    __tablename__ = "calls"
    __table_args__ = {"schema": "events"}
    ts = Column(DateTime, primary_key=True)
    msisdn = Column(String, primary_key=True)
    val = Column(Integer)


class Sms(Base):
    __tablename__ = "sms"
    __table_args__ = {"schema": "events"}
    ts = Column(DateTime, primary_key=True)
    msisdn = Column(String, primary_key=True)
    val = Column(Integer)


class Topup(Base):
    __tablename__ = "topup"
    __table_args__ = {"schema": "events"}
    ts = Column(DateTime, primary_key=True)
    msisdn = Column(String, primary_key=True)
    val = Column(Integer)


class Mds(Base):
    __tablename__ = "mds"
    __table_args__ = {"schema": "events"}
    ts = Column(DateTime, primary_key=True)
    msisdn = Column(String, primary_key=True)
    val = Column(Integer)
