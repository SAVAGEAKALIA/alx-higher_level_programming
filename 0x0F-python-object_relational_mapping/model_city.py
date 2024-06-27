#!/usr/bin/python3
""" Python Database Using Sqlalchemy """

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ Data base code testing Sql """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
