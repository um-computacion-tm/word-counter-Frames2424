import unittest
from count_letters_and_words import Count

class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        countLtr = Count()
        result = countLtr.count_letters('f')
        self.assertEqual(result, {'f': 1})

    def test_complex(self):
        countLtr = Count()
        result = countLtr.count_letters('Hola')
        self.assertEqual(
            result,
            {
                'h': 1,
                'o': 1,
                'l': 1,
                'a': 1,
            }
        )

    def test_super_complex_I(self):
        countLtr = Count()
        result = countLtr.count_letters('¿Como esta?')
        self.assertEqual(
            result,
            {
                'c': 1,
                'o': 2,
                'm': 1,
                'a': 1,
                'e': 1,
                's': 1,
                ' ': 1,
                't': 1,
                '?': 1,
                '¿': 1,
            }
        )

    def test_super_complex_II(self):
        countLtr = Count()
        result = countLtr.count_letters('Honda Tornado 250')
        self.assertEqual(
            result,
            {
                'a': 2,
                'o': 3,
                'd': 2,
                'n': 2,
                't': 1,
                'r': 1,
                '2': 1,
                '5': 1,
                ' ': 2,
                '0': 1,
                'h': 1,

            }
        )

    def test_super_complex_III(self):
        countLtr = Count()
        result = countLtr.count_letters('El mate es una buena razon para estar vivo')
        self.assertEqual(
            result,
            {
                'e': 5,
                'l': 1,
                'm': 1,
                'a': 7,
                's': 2,
                'u': 2,
                'n': 3,
                'b': 1,
                'r': 3,
                'z': 1,
                'p': 1,
                ' ': 8,
                'v': 2,
                'i': 1,
                'o': 2,
                't': 2,
 
                
            }
        )

    def test_super_complex_IV(self):
        countLtr = Count()
        result = countLtr.count_letters('tengo un perro gordote')
        self.assertEqual(
            result,
            {
                't': 2,
                'e': 3,
                'n': 2,
                'g': 2,
                'u': 1,
                'p': 1,
                'r': 3,
                'd': 1,
                'o': 4,
                ' ': 3,
            }
        )

    def test_super_complex_V(self):
        countLtr = Count()
        result = countLtr.count_letters('when cows fly')
        self.assertEqual(
            result,
            {
                'w': 2,
                'h': 1,
                'e': 1,
                'n': 1,
                'c': 1,
                'o': 1,
                's': 1,
                'f': 1,
                'l': 1,
                'y': 1,
                ' ': 2
            }
        )
    def test_super_complex_VI(self):
        countLtr = Count()
        result = countLtr.count_letters('I want you baby')
        self.assertEqual(
            result,
            {
                'i': 1,
                'w': 1,
                'n': 1,
                't': 1,
                ' ': 3,
                'y': 1,
                'o': 1,
                'b': 2,
                'a': 2,
                'y': 2,
                'u': 1

            }
        )

    def test_super_complex_VII(self):
        countLtr = Count()
        result = countLtr.count_letters('my gf is redhead')
        self.assertEqual(
            result,
            {
                'm': 1,
                'y': 1,
                'g': 1,
                'f': 1,
                'i': 1,
                's': 1,
                'r': 1,
                'e': 2,
                'd': 2,
                'h': 1,
                'a': 1,


            }
        )

    def test_super_complex_VII(self):
        countLtr = Count()
        result = countLtr.count_letters('If you read this you will be bauld')
        self.assertEqual(
            result,
            {
                'i': 3,
                'f': 1,
                'y': 2,
                'e': 2,
                'a': 2,
                'l': 3,
                'w': 1,
                ' ': 7,
                'o': 2,
                's': 1,
                'h': 1,
                'u': 3,
                'r': 1,
                't': 1,
                'b': 2,
                'd': 2

            }
        )


class TestCountWords(unittest.TestCase):

    def test_simple(self):
        countWrd = Count()
        result = countWrd.count_words('hola')
        self.assertEqual(result, {'hola': 1})

    def testCountWords_I(self):
        countWrd = Count()
        result = countWrd.count_words('chori flan')
        self.assertEqual(result, {'chori': 1, 'flan': 1})

    def testCountWords_II(self):
        countWrd = Count()
        result = countWrd.count_words('grow up')
        self.assertEqual(result, {'grow': 1, 'up': 1})

    def testCountWords_III(self):
        countWrd = Count()
        result = countWrd.count_words('la policia es corrupta policia policia')
        self.assertEqual(result, {'policia': 3, 'es': 1, 'corrupta': 1, 'la':1 })
    
    def testCountWords_IV(self):
        countWrd = Count()
        result = countWrd.count_words('triunfo seguro')
        self.assertEqual(result, {'triunfo': 1, 'seguro': 1})

    def testCountWords_V(self):
        countWrd = Count()
        result = countWrd.count_words('Las tortafritas llevan grasa de vaca hecha con vaca')
        self.assertEqual(result, {'tortafritas': 1, 'las': 1, 'llevan': 1, 'grasa': 1, 'de': 1, 'vaca': 2, 'hecha': 1, 'con': 1})

    def testCountWords_VI(self):
        countWrd = Count()
        result = countWrd.count_words('quiero una xr 150 una xr 250 una xr 450 una xr 650')
        self.assertEqual(result, {'quiero': 1, 'una': 4, 'xr': 4, '150': 1, '250': 1, '450': 1, '650': 1, })

    def testCountWords_VII(self):
        countWrd = Count()
        result = countWrd.count_words('Milei presidente 2023')
        self.assertEqual(result, {'milei':1, 'presidente': 1, '2023' : 1  })
    
    def testCountWords_VIII(self):
        countWrd = Count()
        result = countWrd.count_words('he-morido')
        self.assertEqual(result, {
            'he-morido':1
            })

if __name__ == '__main__':
    unittest.main()
