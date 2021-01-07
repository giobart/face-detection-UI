import base64
from config import UPLOAD_URL
import requests


def direct_image_upload(file, name, surname, id):
    imagebase64 = base64.b64encode(file.read()).decode('utf-8')
    request_body = {
        "name": str(name),
        "surname": str(surname),
        "img_base64": imagebase64
    }

    response = requests.post(UPLOAD_URL + "/api/store/" + id, json=request_body)

    if response.status_code is not 200:
        raise Exception("Upload failed")
