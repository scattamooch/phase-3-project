from sqlalchemy import Column, Integer, String
from exports import Base
from races import Race
from char_class import Char_Class

class Character(Base, Race, Char_Class):
    __tablename__ = "characters"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    level = Column(Integer())
    hitpoints = Column(Integer())