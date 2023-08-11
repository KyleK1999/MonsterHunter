from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    attack = Column(Integer)
    defense = Column(Integer)
    health = Column(Integer)
    default_health = Column(Integer)

    action_rounds = relationship("ActionRound", back_populates="character")
    inventory_items = relationship("Inventory", back_populates="character")

class Monster(Base):
    __tablename__ = 'monsters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    attack = Column(Integer)
    defense = Column(Integer)
    health = Column(Integer)
    monster_default_health = Column(Integer)

class ActionRound(Base):
    __tablename__ = 'action_rounds'
    
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    action = Column(String)
    value = Column(Integer)

    character = relationship("Character", back_populates="action_rounds")

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    

    owned_by = relationship("Inventory", back_populates="item")

class Inventory(Base):
    __tablename__ = 'inventory'
    
    character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)

    character = relationship("Character", back_populates="inventory_items")
    item = relationship("Item", back_populates="owned_by")
