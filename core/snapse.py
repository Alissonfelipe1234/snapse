import hashlib
from PIL import Image
import io


def resize(image_bytes, width, height):
    image_key = hashlib.md5(image_bytes).hexdigest()
    image_path = 'images/' + image_key + '.png'
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((width, height), Image.ANTIALIAS)
    image.save(image_path)
