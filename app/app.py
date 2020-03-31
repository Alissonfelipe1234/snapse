from flask import Flask, request, jsonify
from PIL import Image
import io
import cv2
import hashlib

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    s = {'/': 'home', '/send': 'route to send images', '/test': 'test request'}
    return jsonify(valid_paths=s), 200


@app.route('/send', methods=['POST'])
def send():
    try:
        image_bytes = request.data
        if image_bytes == b'':
            return jsonify(message='Envie uma imagem'), 418
        if not request.content_type.startswith('image'):
            return jsonify(message='Envie uma imagem valida'), 415
        image_key = hashlib.md5(image_bytes).hexdigest()
        image_path = image_key + '.png'
        image = Image.open(io.BytesIO(image_bytes))
        image = cv2.resize(image, (384, 384))
        image.save(image_path)
        return jsonify(file_name=image_path), 201
    except Exception as exception:
        print(str(exception))
        return jsonify(message='algum erro ocorreu, tente novamente como binary data'), 500


@app.route('/test', methods=['GET'])
def test():
    return jsonify(message="all right"), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
