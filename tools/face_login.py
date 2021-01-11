import requests
from config import *


def face_login_request(base64, img_crop=False):
    response = requests.post(UPLOAD_URL + "/api/find_match", json={'image_base64': base64, 'img_crop': img_crop})

    if response.status_code is not 200:
        message = "nothing found, status code: " + str(response.status_code) + "!"
        raise Exception(message)

    return response.json()
