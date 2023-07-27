from pydantic import BaseModel

# Define your models here


class User(BaseModel):
    username: str
    password: str


class Item(BaseModel):
    name: str
    price: float
    is_active: bool = True