from .database import Base
from sqlalchemy import Column, Integer, String , Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable= False)
    name = Column(String, nullable = False )
    image_link = Column(String, nullable = False)
    # rating = Column(Integer, nullable = False)
    # published =  Column(Boolean, server_default  = 'True',nullable=False)
    price = Column(Integer, nullable= False)
    stock = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable= False)
    email = Column(String, nullable = False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String)

class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, nullable= False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable= False)
    owner = relationship("User")

    pr_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable= False)
    owner = relationship("Product")

    quantity = Column(Integer, nullable=False)

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, nullable= False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable= False)
    owner = relationship("User")

    pr_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable= False)
    owner = relationship("Product")
    
    pr_quantity = Column(Integer, nullable= False)

    status = Column(String, nullable=False)









