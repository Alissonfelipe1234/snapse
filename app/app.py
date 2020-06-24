from flask import Flask, request, jsonify
from controllers.runner import Runner

app = Flask(__name__)
runner = Runner()


@app.route('/', methods=['GET'])
def index():
    s = {
        '/': 'home',
        '/resize': 'resize images, use header width and height',
        '/filter/<kinds>': 'filter images, kinds'
        '(blur, contour, detail, emboss, edges),',
        '/test': 'test request'
    }
    return jsonify(valid_paths=s), 200


@app.route('/filter/<kind>', methods=['POST'])
def filters(kind):
    image_bytes = request.data
    if image_bytes == b'':
        return jsonify(message='send a image'), 418
    content = request.content_type
    if not content or not content.startswith('image'):
        return jsonify(message='send a valid image'), 415
    name = runner.formater(image_bytes, kind)
    return jsonify(file_name=name), 201


@app.route('/resize', methods=['POST'])
def resize():
    image_bytes = request.data
    if image_bytes == b'':
        return jsonify(message='send a image'), 418
    content = request.content_type
    if not content or not content.startswith('image'):
        return jsonify(message='send a valid image'), 415
    try:
        width = int(request.headers['width'])
    except Exception as identifier:
        print(identifier)
        return jsonify(message='use the width`s header'), 418

    try:
        height = int(request.headers['height'])
    except Exception as identifier:
        print(identifier)
        return jsonify(message='use the height`s header'), 418

    name = runner.resize(image_bytes, width, height)
    return jsonify(file_name=name), 201


@app.route('/test', methods=['GET'])
def test():
    return jsonify(message="all right"), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, threaded=True)
