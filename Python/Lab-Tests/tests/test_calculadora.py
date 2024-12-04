try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '../src'
            )
        )
    )
except:
    raise 'Não funciono'

import unittest
from doctest_calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_retorna_10(self):
       self.assertEqual(soma(5,5), 10)

    def test_soma_0_ponto_9_e_0_ponto_9_retorna_1_ponto_8(self):
        self.assertEqual(soma(0.9,0.9), 1.8)

    def test_soma_varios_valores(self):
        x_y_total = (
            (8,5,13),
            (2,6,8),
            (4,4,8),
            (10,10,20)
        )

        for calculo in x_y_total:
            with self.subTest(calculo=calculo):
                x, y, total = calculo
                self.assertEqual(soma(x,y),total)

    def test_soma_tipo_de_x_retorna_int_ou_float_se_nao_retorna_assert(self):
        with self.assertRaises(TypeError):
            soma('a',2)
    
    def test_soma_tipo_de_y_retorna_int_ou_float_se_nao_retorna_assert(self):
        with self.assertRaises(TypeError):
            soma(2,'a')

if __name__ == "__main__":
    unittest.main(verbosity=2)
