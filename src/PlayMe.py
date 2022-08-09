import requests
import os
import time
from progress.bar import Bar
import json
from pprint import pprint
from DownloadsPhoto import DownloadsPhoto
from DownloadsPhoto import token_vk
from UploadPhoto import UploadPhoto
from UploadPhoto import token_yandex

if __name__ == '__main__':
    user1 = UploadPhoto(token_yandex)
    user1.uploading_files_to_yandex_disk(user1.creating_a_new_folder_on_yandex_disk('Фотки с Vk'))
    user1 = DownloadsPhoto(id, token_vk)
    user1.downloads_photo_from_vk()