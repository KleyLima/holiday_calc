# -*- coding: utf-8 -*-

from datetime import date, timedelta
from sys import argv, exit
from re import sub


class CalcData:
    def __init__(self, year):
        """Método que inicializa o objeto e seu valor de ano"""
        self.year = year
        self.cleaner()
        self.check()
        if self.valid:
            self.pascoa()
            self.carnaval()
            self.corpus_christi()
            self.holy_friday()

    def pascoa(self):
        """Método que calcula a data da Páscoa baseada no algoritmo de Meeus/Jones/Butcher"""
        if self.valid == True:
            alfa = self.year % 19
            beta = self.year // 100
            charlie = self.year % 100
            delta = beta // 4
            echo = beta % 4
            fox = (beta + 8) // 25
            golf = (beta - fox + 1) // 3
            hotel = (19 * alfa + beta - delta - golf + 15) % 30
            india = charlie // 4
            kilo = charlie % 4
            lima = (32 + 2 * echo + 2 * india - hotel - kilo) % 7
            mike = (alfa + 11 * hotel + 22 * lima) // 451
            self.month = (hotel + lima - 7 * mike + 114) // 31
            self.day = 1 + (hotel + lima - 7 * mike + 114) % 31
            self.pascoa = date(self.year, self.month, self.day)
        else:
            return False

    def carnaval(self):
        """Método que calcula a data do Carnaval com referência na data da Páscoa"""
        self.carnaval = self.pascoa - timedelta(days=47)

    def corpus_christi(self):
        """"Método que calcula a data de Corpus Christi com base na data da Páscoa"""
        self.corpus = self.pascoa + timedelta(days=60)

    def holy_friday(self):
        """Método que calcula a data da Sexta-Feira Santa com base na data da Páscoa"""
        self.friday = self.pascoa - timedelta(days=2)

    def print_datas(self):
        """Método para formatar a data para DD-MM-YYYY e printa-las. """
        if self.valid:
            print('Carnaval: {}'.format(self.carnaval.strftime('%d/%m/%Y')))
            print('Sexta-Feira Santa: {}'.format(self.friday.strftime('%d/%m/%Y')))
            print('Páscoa: {}'.format(self.pascoa.strftime('%d/%m/%Y')))
            print('Corpus Christi: {}'.format(self.corpus.strftime('%d/%m/%Y')))
            return True
        else:
            print('Valor Inválido')

    def check(self):
        """
        Método para checar se o ano recebido é válido para o cálculo da Páscoa, que é a base dos outros 
        feriados.
        """
        self.valid = True if self.year > 1583 else False

    def cleaner(self):
        """Método que limpa a informação recebida, deixando apenas números"""
        clean = sub('\D', '', str(self.year))
        self.year = int(clean) if clean != '' else 0

if __name__ == '__main__':
    if argv[1:]:
        data = CalcData(argv[1])
    else:
        data = CalcData(input('Ano:'))
    data.print_datas()
