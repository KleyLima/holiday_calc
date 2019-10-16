# -*- coding: utf-8 -*-

import unittest
from source.calc_data3 import CalcData

class TestCalcData(unittest.TestCase):

    def test_cleaner(self):
        """Testa o método que limpa caracteres indesejados da entrada"""
        self.assertEqual(CalcData('abc2019abc').year, 2019)
        self.assertEqual(CalcData('2019a.c').year, 2019)
        self.assertNotEqual(CalcData('-2019').year, -2019)

    def test_checker(self):
        """Testa o método que valida o ano para o calculo da Páscoa"""
        self.assertTrue(CalcData('2015').valid)
        self.assertFalse(CalcData('1500').valid)

    def test_printer(self):
        """Testa o comportamento do método de output quando a entrada não é válida"""
        self.assertTrue(CalcData('2015').print_datas())
        self.assertFalse(CalcData('1500').print_datas())

    def test_pascoa(self, year = 1590):
        """Testa se a data calculada da Páscoa coincide com o Domingo no período de 1590 a 2500 """
        self.assertEqual((CalcData(year).pascoa).weekday(), 6)
        year+=1
        if year <= 2500: TestCalcData().test_pascoa(year)

    def test_friday(self, year = 1590):
        """Testa se a data calculada da sexta feira santa coincide com a Sexta-Feira de 1590 a 2500 """
        self.assertEqual(CalcData(year).friday.weekday(), 4)
        year+=1
        if year <= 2500: TestCalcData().test_friday(year)

    def test_carnaval(self, year = 2000):
        """Testa se a data calculada do Carnaval coincide com a terça-feira no periodo de 2000 a 2800"""
        self.assertEqual(CalcData(year).carnaval.weekday(), 1)
        year+=1
        if year <= 2800: TestCalcData().test_carnaval(year)

    def test_corpus(self, year = 2000):
        """Testa se a data calculada para o Corpus Christi coincide com a quinta-feira no periodo de 2000 a 2800"""
        self.assertEqual(CalcData(year).corpus.weekday(), 3)
        year+=1
        if year <= 2800: TestCalcData().test_corpus(year)


if __name__ == '__main__':
    unittest.main()
