from typing import List
from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks
from .schemas import GetImage, Message, GetListImage
from .models import Image
from .services import load_into_db

service_router = APIRouter()


@service_router.post("/")
async def create_image(
        background_tasks: BackgroundTasks,
        title: str = Form(),
        description: str = Form(),
        file: UploadFile = File()
):
    return await load_into_db(background_tasks, title, description, file)


@service_router.get("/img/{image_pk}", response_model=GetImage, responses={404: {'model': Message}})
async def get_image(image_pk: int):
    return await Image.objects.select_related('user').get(pk=image_pk)


@service_router.get("/user/{user_pk}", response_model=List[GetListImage], responses={404: {'model': Message}})
async def get_list_image(user_pk: int):
    image_list = await Image.objects.filter(user=user_pk).all()
    return image_list