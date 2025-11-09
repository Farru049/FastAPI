from sqlalchemy import Column, String, Integer
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True, index = True, nullable = False)
    name = Column(String, nullable = False)
    age = Column(Integer, nullable=False, index=True)
    email = Column(String, unique=True, index=True, nullable=False)

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key = True, index = True, nullable = False)
    name = Column(String, nullable = False)
    price = Column(Integer, nullable = False)
    description = Column(String, nullable=True)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key= True, index = True, nullable= False)
    content = Column(String, nullable = False)
    rating = Column(Integer, nullable = False)