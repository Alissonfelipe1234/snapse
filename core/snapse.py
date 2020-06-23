import hashlib
from PIL import Image, ImageFilter
import io

filters = {
            'blur': ImageFilter.BLUR,
            'contour': ImageFilter.CONTOUR,
            'detail': ImageFilter.DETAIL,
            'emboss': ImageFilter.EMBOSS,
            'edges': ImageFilter.FIND_EDGES
          }


def path(name):
    return 'images/' + name + '.png'


def resize(image_bytes, width, height):
    name = image_bytes + bytes(width) + bytes(height)
    name = hashlib.md5(name).hexdigest()
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((width, height), Image.ANTIALIAS)
    image.save(path(name))


def formater(image_bytes, kind):
    name = image_bytes + bytes(kind, encoding='utf-8')
    name = hashlib.md5(name).hexdigest()
    image = Image.open(io.BytesIO(image_bytes))
    image = image.filter(filters.get(kind))
    image.save(path(name))
