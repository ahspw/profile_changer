from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon import TelegramClient
from random import choice
import sys
import os

# Get api_id and api_hash from https://my.telegram.org

path = r"" # location of photos that are going to be uploaded 
api_id = ""
api_hash = ""
telegram_client_name = "" # a name for session's logs file

uploaded_images = []

def select_image():
    while True:
        images_list = os.listdir(path)
        image_name = choice(images_list)
        if image_name not in uploaded_images:
            image_path = path+image_name
            return image_path

client = TelegramClient(f"{telegram_client_name}", api_id, api_hash)
async def upload():
    await client(UploadProfilePhotoRequest(
        await client.upload_file(select_image())
    ))

async def delete():
    await client(DeletePhotosRequest(await client.get_profile_photos("me")))


with client:
    client.loop.run_until_complete(delete())
    client.loop.run_until_complete(upload())