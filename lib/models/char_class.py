from sqlalchemy import Column, Integer, String
from exports import Base

class Char_Class(Base):
    __tablename__ = "classes"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    armor = Column(String())
    weapon = Column(String())
    starting_gear = Column(String())
