
from PIL import Image
import io


def resize(image_bytes, width, height, name):
    image_path = 'images/' + name + '.png'
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((width, height), Image.ANTIALIAS)
    image.save(image_path)
