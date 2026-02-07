from pydantic import BaseModel, Field
from typing import Any

from enum import Enum

class Gender(Enum):
    male = "male"
    female = "female"

class UserCreate(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=100)
    description: str | None
    age: int = Field(ge=14, gt=150)
    gender: Gender
    
class User(UserCreate):
    ...

class UserForm(BaseModel):
    name: str
    description: str
    age: int 
    geo: Any
    