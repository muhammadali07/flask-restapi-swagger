from app.db import Base
from sqlalchemy import (
    Column, Integer, 
    String, BigInteger, 
    ForeignKey, Date, 
    DateTime, Numeric, 
    Boolean, Float,
    TIMESTAMP, Text,
    )
from sqlalchemy.sql import func

class Products(Base):

    __tablename__ = 'products'

    id = Column(String(36), primary_key = True)
    name = Column(String(200))
    description = Column(String(200))
    images = Column(String(200))
    logo_id = Column(Integer)
    create_at = Column(TIMESTAMP, server_default=func.now())    
    update_at = Column(TIMESTAMP) 

class Variant(Products):
    __tablename__ = 'variants'

    id = Column(String(36), primary_key = True)
    product_id = Column(BigInteger, ForeignKey("products.id"), autoincrement=True)
    name = Column(String(100))
    size = Column(Integer)
    color = Column(String(100))
    images = Column(String(100))
    create_at = Column(TIMESTAMP, server_default=func.now())    
    update_at = Column(TIMESTAMP) 

class Image(Base):
    __tablename__ = 'variants'

    id = Column(String(36), primary_key = True)
    url = Column(Text)

