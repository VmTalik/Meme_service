import shutil
from fastapi import APIRouter, UploadFile, File, Form, Request, BackgroundTasks, HTTPException
from schemas import UploadImage, GetImage, Message
from fastapi.responses import JSONResponse
from models import Image, User
from services import save_image

service_router = APIRouter()


@service_router.post("/")
async def create_image(
        background_tasks: BackgroundTasks,
        title: str = Form(),
        description: str = Form(),
        file: UploadFile = File()
):
    file_name = f'media/{file.filename}'
    if file.content_type == 'image/jpeg':
        background_tasks.add_task(save_image, file_name, file)
    else:
        raise HTTPException(status_code=404, detail='Формат файла не jpeg !')
    info = UploadImage(title=title, description=description)
    user = await User.objects.first()
    return await Image.objects.create(file=file.filename, user=user, **info.dict())


@service_router.get("/img/{image_pk}", response_model=GetImage, responses={404: {'model': Message}})
async def get_image(image_pk: int):
    return await Image.objects.select_related('user').get(pk=image_pk)
