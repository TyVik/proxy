import unittest

from processors import set_tm


class ProcessorTestCase(unittest.TestCase):
    def test_set_tm(self):
        example = 'Client web client.Client wrong connection client.'
        result = set_tm(example, '^')
        self.assertEqual(result, 'Client^ web client^.Client^ wrong connection client^.')

        example = 'Тостер'
        result = set_tm(example, '^')
        self.assertEqual(result, 'Тостер^')

if __name__ == '__main__':
    unittest.main()