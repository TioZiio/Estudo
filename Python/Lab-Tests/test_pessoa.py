import unittest
from unittest.mock import patch
from Pessoas import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Tio', 'Ziio')

    def test_pessoa_attr_name_tem_o_valor_correto(self):
        self.assertEqual(self.p1.name, 'Tio')

    def test_pessoa_attr_name_e_str(self):
        self.assertIsInstance(self.p1.name, str)

    def test_pessoa_attr_lastname_tem_o_valor_correto(self):
        self.assertEqual(self.p1.lastname, 'Ziio')

    def test_pessoa_attr_lastname_e_str(self):
        self.assertIsInstance(self.p1.lastname, str)
    
    def test_pessoa_attr_data_tem_o_valor_false(self):
        self.assertFalse(self.p1.data)

    def test_pessoa_capturou_os_dados_OK(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
