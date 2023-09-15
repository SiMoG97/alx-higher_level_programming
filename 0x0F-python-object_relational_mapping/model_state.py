#!/usr/bin/python3
"""
    Module that defines a State class
    that represents a states table in the database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents a states table in the database

    Attributes:
        id (int): state id
        name (str): state name
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
