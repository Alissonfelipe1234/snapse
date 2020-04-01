from flask import Flask, request, jsonify
from controllers.runner import Runner

app = Flask(__name__)
runner = Runner()


@app.route('/', methods=['GET'])
def index():
    s = {'/': 'home', '/send': 'route to send images', '/test': 'test request'}
    return jsonify(valid_paths=s), 200


@app.route('/send', methods=['POST'])
def send():
    image_bytes = request.data
    if image_bytes == b'':
        return jsonify(message='Envie uma imagem'), 418
    if not request.content_type.startswith('image'):
        return jsonify(message='Envie uma imagem valida'), 415
    name = runner.send(image_bytes)
    return jsonify(file_name=name), 201


@app.route('/test', methods=['GET'])
def test():
    return jsonify(message="all right"), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, threaded=True)
