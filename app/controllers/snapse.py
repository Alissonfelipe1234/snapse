import cv2
import hashlib
from PIL import Image
import io


def resize(image_bytes):
    image_key = hashlib.md5(image_bytes).hexdigest()
    image_path = image_key + '.png'
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((384, 384), Image.ANTIALIAS)
    image.save(image_path)
    return image_path
