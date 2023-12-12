#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'Student'

    id = Column (Integer(), Primary_key = True)
    name = Column (String())
    pass

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.Create_all(engine)
    pass