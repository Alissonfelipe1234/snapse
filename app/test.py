import hashlib
import unittest
from app import app


class ApiTestCase(unittest.TestCase):
    def test_api_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        expected = b'{"valid_paths":{"/":"home",' + \
            b'"/send":"route to send images","/test":"test request"}}\n'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)

    def test_api_test(self):
        tester = app.test_client(self)
        response = tester.get('/test', content_type='application/json')
        expected = b'{"message":"all right"}\n'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)

    def test_api_send(self):
        tester = app.test_client(self)
        content = 'image/jpg'
        binary = b'zeros_e_uns'
        name_file = hashlib.md5(binary).hexdigest()
        response = tester.post('/send', content_type=content, data=binary)
        expected = '{"file_name":"' + name_file + '.png"}\n'
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.decode('utf-8'), expected)

    def test_api_send_empty(self):
        tester = app.test_client(self)
        content = 'application/json'
        response = tester.post('/send', content_type=content)
        expected = b'{"message":"Envie uma imagem"}\n'
        self.assertEqual(response.status_code, 418)
        self.assertEqual(response.data, expected)

    def test_api_send_invalid(self):
        tester = app.test_client(self)
        content = 'application/json'
        response = tester.post('/send', content_type=content, data=b'imagem')
        expected = b'{"message":"Envie uma imagem valida"}\n'
        self.assertEqual(response.status_code, 415)
        self.assertEqual(response.data, expected)


if __name__ == '__main__':
    unittest.main()
