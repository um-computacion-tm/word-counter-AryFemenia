#IMPORTS
import unittest
from letter_count import count_letters
from word_count import count_words

#TEST LETTER COUNT
class TestCountLetters(unittest.TestCase):
    def test_letter_simple_1(self):
        result = count_letters('a')
        self.assertEqual(result, {'a': 1})
    def test_letter_simple_2(self):
        result = count_letters('b')
        self.assertEqual(result, {'b': 1})

    def test_letter_complex_1(self):
        result = count_letters('aaabcd')
        self.assertEqual(
            result,
            {
                'a': 3,
                'b': 1,
                'c': 1,
                'd': 1,
            }
        )

    def test_letter_super_complex_1(self):
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
    def test_word_1(self):
        result = count_words('saracatunga')
        result_god = {'saracatunga': 1}
        self.assertEqual(result_god, result)
    def test_word_2(self):
        result = count_words('Gabe Newell')
        result_god = {'Gabe': 1,
                      'Newell': 1
                      }
        self.assertEqual(result_god, result)
    def test_word_3(self):
        result = count_words('hola que hola')
        result_god = {'hola': 2,
                      'que': 1}
        self.assertEqual(result_god, result)
    def test_word_4(self):
        result = count_words('god god god god god')
        result_god = {'god': 5}
        self.assertEqual(result_god, result)
    def test_word_5(self):
        result = count_words('god have mercy')
        result_god = {'god': 1,
                      'have': 1,
                      'mercy': 1
                      }
        self.assertEqual(result_god, result)

if __name__ == '__main__':
    unittest.main()
