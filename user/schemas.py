from fastapi_users import schemas


class User(schemas.BaseUser):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(User, schemas.BaseUserUpdate):
    pass


# class UserDB(User, schemas.BaseUserDB):
#     pass