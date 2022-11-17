import datetime
from typing import Optional

import ormar
from db import database, metadata


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=60)


class Image(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=45)
    description: str = ormar.String(max_length=300)
    file: str = ormar.String(max_length=800)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    user:Optional[User] = ormar.ForeignKey(User)
