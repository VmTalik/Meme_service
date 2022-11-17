import shutil
from fastapi import UploadFile


def save_image(file_name: str, file: UploadFile):
    """Функция для сохранения(записи) файла на диск"""
    with open(file_name, 'wb') as f:
        shutil.copyfileobj(file.file, f)
