from typing import Optional, List # Supports for type hints
from pydantic import BaseModel # Most widely used data validation library for python
from enum import Enum # Supports for enumerations

# enum for gender
class Gender(str, Enum):
    male = "male"
    female = "female"

# enum for role
class Role(str, Enum):
    admin = "admin"
    student = "student"
    faculty = "faculty"

class User(BaseModel):
    user_name: str
    password:str
    roles: List[Role] # user can have several roles
    
class UserCollection(BaseModel):
    users: List[User]