import base64
from config import UPLOAD_URL
import requests


def users_list(page):
    response = requests.get(UPLOAD_URL + "/api/get_all/30/" + str(page))

    if response.status_code is not 200:
        raise Exception("fail")

    return response.json()["users"]


def delete_user(id):
    response = requests.delete(UPLOAD_URL + "/api/" + str(id))
    if response.status_code is not 200:
        raise Exception("fail")
