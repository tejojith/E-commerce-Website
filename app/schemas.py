from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class Product(BaseModel):

    id: int
    name: str
    img_link: str
    price: int
    stock: int 
    size: str
    gender: str
    category: str

    class Config:
        orm_model = True

class ProductCreate(Product):
    pass





class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    created_at: datetime
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Cart(UserOut):
    id: str




