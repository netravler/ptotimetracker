from pydantic import BaseModel
from datetime import date

class UserLogin(BaseModel):
    username: str
    password: str

class PTORequest(BaseModel):
    date: date
    type: str
