import unittest
import hashlib
import snapse


class ApiTestCase(unittest.TestCase):
    def test_api_test(self):
        with open('../images/marie_curie.jpg', 'rb') as img:
            binary = img.read()
            snapse.resize(binary, 200, 200)
            file_name = './images/' + hashlib.md5(binary).hexdigest() + '.png'
            with open(file_name, 'rb') as small_img:
                self.assertIsNotNone(small_img)


if __name__ == '__main__':
    unittest.main()
