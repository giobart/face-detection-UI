import requests
from config import *


def face_login_request(base64, img_crop=False, liveness=False, frames=[]):
    response = requests.post(UPLOAD_URL + "/api/find_match", json={'image_base64': base64, 'img_crop': img_crop, 'liveness':liveness, 'frames':frames})

    if response.status_code is not 200:
        message = "Login Failed: " + str(response.text) + "!"
        raise Exception(message)

    return response.json()
