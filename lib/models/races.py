from sqlalchemy import Column, Integer, String
from exports import Base

class Race(Base):
    __tablename__ = "races"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    size = Column(Integer())
    age = Column(Integer())
    language = Column(String())