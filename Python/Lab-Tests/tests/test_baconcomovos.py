"""
TDD - Test Driven Development (Desenvolvimento dirigido a testes)

Red:
    Parte 1 -> Criar e o Teste e ver falhar.

Green:
    Parte 2 -> Criar e o Teste e ver sucesso.

Refactor
    Parte 3 -> Melhorar o código.
"""
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
from baconcomovos import bacon_com_ovos

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_retorn_AssertError_se_not_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('2')

    def test_bacon_com_ovos_return_multiplo_de_3_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com Ovos'

        for v in entradas:
            with self.subTest(entrada=v, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(v).upper(),
                    saida.upper(),
                    msg=f'\n\t{v} não retornou {saida}!!!')

    def test_bacon_com_ovos_return_fica_com_fome_se_not_multiplo_de_3_e_5(self):
        entradas = (1,2,4,7,8)
        saida = 'Fica com fome'

        for v in entradas:
            with self.subTest(entrada=v, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(v).upper(),
                    saida.upper(),
                    msg=f'\n\tCom {v} voce {saida}!!!')

    def test_bacon_com_ovos_return_bacon_se_multiplo_de_3(self):
        entradas = (3,6,9,12)
        saida = 'Bacon'

        for v in entradas:
            with self.subTest(entrada=v, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(v).upper(),
                    saida.upper(),
                    msg=f'\n\tCom {v} voce come {saida}')

    def test_bacon_com_ovos_return_ovos_se_multiplo_de_5(self):
        entradas = (5,10,20,25)
        saida = 'ovos'

        for v in entradas:
            with self.subTest(entrada=v, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(v).upper(),
                    saida.upper(),
                    msg=f'\n\tCom {v} voce come {saida}')

if __name__ == "__main__":
    unittest.main(verbosity=2)
