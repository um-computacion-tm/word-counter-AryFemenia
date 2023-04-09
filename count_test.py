#IMPORTS
import unittest
from letter_count import count_letters
from word_count import count_words

#TEST LETTER COUNT
class TestCountLetters(unittest.TestCase):
    def test_simple(self):
        result = count_letters('a')
        self.assertEqual(result, {'a': 1})
    def test_complex(self):
        result = count_letters('hola')
        self.assertEqual(
            result,
            {
                'h': 1,
                'o': 1,
                'l': 1,
                'a': 1,
            }
        )
    def test_super_complex(self):
        result = count_letters('hola chau')
        self.assertEqual(
            result,
            {
                'h': 2,
                'o': 1,
                'l': 1,
                'a': 2,
                ' ': 1,
                'c': 1,
                'u': 1
            }
        )

#TEST WORD COUNT
class TestCountWords(unittest.TestCase):
    def test_simple(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})

if __name__ == '__main__':
    unittest.main()