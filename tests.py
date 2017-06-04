import unittest

from bs4 import BeautifulSoup

from processors import set_tm, modify_links


class ProcessorTestCase(unittest.TestCase):
    def test_modify_links(self):
        example = '<div><a></a><a href="http://old.com/all/">Text</a></div>'
        soup = BeautifulSoup(example, "html.parser")
        result = modify_links(soup, 'http://old.com', 'https://new.com')
        self.assertEqual(str(result), '<div><a></a><a href="https://new.com/all/">Text</a></div>')

    def test_set_tm(self):
        example = 'Client web client.Client wrong connection client.'
        result = set_tm(example, '^')
        self.assertEqual(result, 'Client^ web client^.Client^ wrong connection client^.')

        example = 'Тостер'
        result = set_tm(example, '^')
        self.assertEqual(result, 'Тостер^')

if __name__ == '__main__':
    unittest.main()