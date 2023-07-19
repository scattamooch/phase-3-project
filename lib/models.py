from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
# from sqlalchemy.ext.declarative import 

Base = declarative_base()
engine = create_engine("sqlite:///tbdnd.db")
Session = sessionmaker(bind=engine)

session = Session()

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    level = Column(Integer())
    char_skill = Column(String())
    char_class_id = Column(ForeignKey("char_classes.id"))
    race_id = Column(ForeignKey("races.id"))

    char_class = relationship("CharClass", backref="characters")
    race = relationship("Race", backref = "characters")


class CharClass(Base):
    __tablename__ = "char_classes"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    armor = Column(String())
    weapons = Column(String())
    starting_gear = Column(String())

    # characters = relationship("Character", cascade = "all, delete-orphan")
    


class Race(Base):
    __tablename__ = "races"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    size = Column(String())
    language = Column(String())
    skill = Column(String())

    # race = relationship("Race", cascade = "all, delete-orphan")