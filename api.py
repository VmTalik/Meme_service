import shutil
from fastapi import APIRouter, UploadFile, File, Form, Request
from schemas import UploadImage, GetImage, Message
from fastapi.responses import JSONResponse
from models import Image, User

service_router = APIRouter()


@service_router.post("/")
async def create_image(title: str = Form(), description: str = Form(), file: UploadFile = File()):
    info = UploadImage(title=title, description=description)
    with open(f'{file.filename}', 'wb') as f:
        shutil.copyfileobj(file.file, f)
    user = await User.objects.first()
    return await Image.objects.create(file=file.filename, user=user, **info.dict())


@service_router.get("/img/{image_pk}", response_model=GetImage, responses={404: {'model': Message}})
async def get_image(image_pk: int):
    return await Image.objects.select_related('user').get(pk=image_pk)
