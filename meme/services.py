import shutil
from fastapi import UploadFile, HTTPException, BackgroundTasks
from .schemas import UploadImage
from .models import Image
from user.models import User


async def load_into_db(
        background_tasks: BackgroundTasks,
        title: str,
        description: str,
        file: UploadFile
):
    """Функция для загрузки мема в базу данных"""
    file_name = f'media/{file.filename}'
    if file.content_type == 'image/jpeg':
        background_tasks.add_task(save_image, file_name, file)
    else:
        raise HTTPException(status_code=404, detail='Формат файла не jpeg !')
    info = UploadImage(title=title, description=description)
    user = await User.objects.first()
    return await Image.objects.create(file=file_name, user=user, **info.dict())


def save_image(file_name: str, file: UploadFile):
    """Функция для сохранения(записи) файла на диск"""
    with open(file_name, 'wb') as f:
        shutil.copyfileobj(file.file, f)
