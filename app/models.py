# models.py
from pydantic import BaseModel

class Message(BaseModel):
    content: str

class EmergencyRequest(BaseModel):
    description: str

class Location(BaseModel):
    area: str
