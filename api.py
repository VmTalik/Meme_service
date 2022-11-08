import shutil
from fastapi import APIRouter, UploadFile, File, Form, Request
from schemas import UploadImage, GetImage, Message
from fastapi.responses import JSONResponse

service_router = APIRouter()


@service_router.post("/")
async def root(title: str = Form(), description: str = Form(), file: UploadFile = File()):
    info = UploadImage(title=title, description=description)
    with open(f'{file.filename}', 'wb') as f:
        shutil.copyfileobj(file.file, f)
    return {'file_name': file.filename, "info": info}


@service_router.get("/img", response_model=GetImage, responses={404: {'model': Message}})
async def get_image():
    user = {'id': 10, 'name': 'Baron'}
    image = {'title': 'Test', 'description': 'Description'}
    info = GetImage(user=user, image=image)
    # return info
    return JSONResponse(status_code=404, content={'message': 'Item not found'})


@service_router.get("/test")
async def get_test(req: Request):
    # Информация о запросе
    print(req.base_url)
    return {}
