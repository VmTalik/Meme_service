import aiofiles
import shutil
from fastapi import UploadFile


def save_image(file_name: str, file: UploadFile):
    """Асинхронная функция для сохранения(записи) файла на диск"""
    async with aiofiles.open(file_name, 'wb') as f:
        data = await file.read()
        await f.write(data)
    # with open(f'{file.filename}', 'wb') as f:
    #     shutil.copyfileobj(file.file, f)
