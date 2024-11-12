import unittest
from codigo import *  # Importa todas as funções do arquivo 'codigo.py'

class Testes(unittest.TestCase):

    # Testes para a função email_valido
    def test_email_valido(self):
        self.assertTrue(email_valido("teste@exemplo.com"))
        self.assertFalse(email_valido("testeexemplo.com"))
        self.assertFalse(email_valido("teste@com"))

    # Testes para a função eh_par
    def test_eh_par(self):
        self.assertTrue(eh_par(2))
        self.assertFalse(eh_par(3))
        self.assertTrue(eh_par(0))
        self.assertFalse(eh_par(-1))

    # Testes para a função fatorial
    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(7), 5040)

    # Testes para a função quadrado
    def test_quadrado(self):
        self.assertEqual(quadrado(3), 9)
        self.assertEqual(quadrado(4), 16)
        self.assertEqual(quadrado(-2), 4)
        self.assertEqual(quadrado(0), 0)

    # Testes para a função eh_positivo
    def test_eh_positivo(self):
        self.assertTrue(eh_positivo(1))
        self.assertFalse(eh_positivo(-1))
        self.assertFalse(eh_positivo(0))

    # Testes para a função verificar_maioridade
    def test_verificar_maioridade(self):
        self.assertEqual(verificar_maioridade(20), 'maior de idade')
        self.assertEqual(verificar_maioridade(16), 'menor de idade')
        self.assertEqual(verificar_maioridade(18), 'maior de idade')

    # Testes para a função classificar_temperatura
    def test_classificar_temperatura(self):
        self.assertEqual(classificar_temperatura(-5), 'frio')
        self.assertEqual(classificar_temperatura(15), 'moderado')
        self.assertEqual(classificar_temperatura(30), 'quente')

    # Testes para a função avaliar_nota
    def test_avaliar_nota(self):
        self.assertEqual(avaliar_nota(8), 'aprovado')
        self.assertEqual(avaliar_nota(6), 'recuperacao')
        self.assertEqual(avaliar_nota(4), 'reprovado')

    # Testes para a função pode_votar
    def test_pode_votar(self):
        self.assertEqual(pode_votar(20), 'voto obrigatório')
        self.assertEqual(pode_votar(17), 'voto facultativo')
        self.assertEqual(pode_votar(15), 'não pode votar')

    # Testes para a função avaliar_produto
    def test_avaliar_produto(self):
        self.assertEqual(avaliar_produto(5), 'excelente')
        self.assertEqual(avaliar_produto(3), 'regular')
        self.assertEqual(avaliar_produto(1), 'péssimo')
        self.assertEqual(avaliar_produto(6), 'valor inválido')

    # Testes para as funções matemáticas

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

    def test_subtrai(self):
        self.assertEqual(subtrai(5, 3), 2)
        self.assertEqual(subtrai(5, 7), -2)

    def test_multiplica(self):
        self.assertEqual(multiplica(3, 4), 12)
        self.assertEqual(multiplica(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 0), "Erro: divisão por zero não permitida.")

    def test_area_circulo(self):
        self.assertEqual(area_circulo(3), math.pi * 9)
        self.assertEqual(area_circulo(-3), "Erro: o raio não pode ser negativo.")

    def test_area_retangulo(self):
        self.assertEqual(area_retangulo(2, 3), 6)
        self.assertEqual(area_retangulo(-2, 3), "Erro: largura e altura devem ser não-negativos.")

if __name__ == '__main__':
    unittest.main()
