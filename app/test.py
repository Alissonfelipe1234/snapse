import unittest
import io
import hashlib
from app import app


class ApiTestCase(unittest.TestCase):

    def test_api_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        expected = b'{"valid_paths":\
                        {\
                            "/":"home","/send":\
                            "route to send images",\
                            "test":"test request"\
                        }\
                    }'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)

    def test_api_test(self):
        tester = app.test_client(self)
        response = tester.get('/test', content_type='application/json')
        expected = '{"message": "all right"}'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)

    def test_api_send(self):
        tester = app.test_client(self)
        with open('assets/marie_curie.jpg', 'rb') as img.read():
            img = img.read()
            image_name = hashlib.md5(img.hexdigest()
            content = 'application/json'
            response = tester.post('/send', content_type=content, data=img)
        expected = '{"file_name": "' + image_name + '"}'
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, expected)

    def test_api_send_empty(self):
        tester = app.test_client(self)
        content = 'application/json'
        response = tester.post('/send', content_type=content)
        self.assertEqual(response.status_code, 418)
        self.assertEqual(response.data, b'Envie uma imagem')


if __name__ == '__main__':
    unittest.main()
