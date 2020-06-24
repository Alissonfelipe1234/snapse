import unittest
import hashlib
import snapse


class ApiTestCase(unittest.TestCase):
    def test_resize(self):
        with open('./images/marie_curie.jpg', 'rb') as img:
            binary = img.read()
            snapse.resize(binary, 200, 200)
            name = binary + bytes(200) + bytes(200)
            file_name = './images/' + hashlib.md5(name).hexdigest() + '.png'
            with open(file_name, 'rb') as small_img:
                self.assertIsNotNone(small_img)

    def test_filter(self):
        with open('./images/marie_curie.jpg', 'rb') as img:
            binary = img.read()
            snapse.formater(binary, 'blur')
            name = binary + bytes('blur', encoding='utf-8')
            file_name = './images/' + hashlib.md5(name).hexdigest() + '.png'
            with open(file_name, 'rb') as small_img:
                self.assertIsNotNone(small_img)


if __name__ == '__main__':
    unittest.main()
