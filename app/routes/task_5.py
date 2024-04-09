import os
from pathlib import Path
from zipfile import ZipFile

from dulwich.web import send_file
from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter(tags=["API для хранения файлов"])

"""
Задание_5. API для хранения файлов

a.	Написать API для добавления(POST) "/upload_file" и скачивания (GET) "/download_file/{id}" файлов. 
В ответ на удачную загрузку файла должен приходить id для скачивания. 
b.	Добавить архивирование к post запросу, то есть файл должен сжиматься и сохраняться в ZIP формате.
с*.Добавить аннотации типов.
"""

#fakeBd = dict()
#iD = 0


@router.post("/upload_file", description="Задание_5. API для хранения файлов")
async def upload_file(file):
    """Описание."""
    #global iD, fakeBd

    file = open()

    iD += 1
    destination_dir = ''
    fileName = os.path.basename(file).split('/')[-1]
    # Путь для архива
    zipFilePath = os.path.join(destination_dir, os.path.basename(file).split('.')[0] + '.zip')
    # Создаем архив
    with ZipFile(r'archives/' + zipFilePath, 'a') as zipf:
        zipf.write(file, arcname=fileName)
    p = str(Path(zipFilePath).resolve())
    createFile = [zipFilePath, p]
    fakeBd[iD] = createFile
    return iD


@router.get("/download_file/{file_id}", description="Задание_5. API для хранения файлов")
async def download_file(file_id: int):
    """Описание."""
    global iD, fakeBd
    return FileResponse(path=f'{fakeBd[file_id][1]}', filename=f'{fakeBd[file_id][0]}',
                        media_type='application/octet-stream')
