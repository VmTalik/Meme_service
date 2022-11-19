from pydantic import BaseModel

from user.schemas import User


class UploadImage(BaseModel):
    title: str
    description: str


class GetListImage(BaseModel):
    id: int
    title: str
    description: str


class GetImage(GetListImage):
    user: User


class Message(BaseModel):
    message: str
