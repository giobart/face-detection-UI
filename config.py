import os
UPLOAD_URL = os.getenv('K8_IMAGE_REGISTRATION_SERVICE', "http://0.0.0.0:5005")
print("configured UPLOAD_URL ",UPLOAD_URL)
