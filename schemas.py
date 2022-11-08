from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class UploadImage(BaseModel):
    title: str
    description: str
    # tags: List[str]


class GetImage(BaseModel):
    user: User
    image: UploadImage


class Message(BaseModel):
    message: str
