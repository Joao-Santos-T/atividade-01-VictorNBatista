"""
Testes da classe Aluno.
"""
import unittest

from aluno import Aluno


class TestAluno(unittest.TestCase):
    """Testes da classe Aluno."""

    def setUp(self):
        """Cria um aluno base para reutilizar nos testes."""
        self.aluno = Aluno(nome="João", matricula="123")

    def test_adicionar_nota(self):
        """Testa se a nota é adicionada corretamente."""
        self.aluno.adicionar_nota("Matemática", 8.0)
        self.assertIn("Matemática", self.aluno.notas)
        self.assertEqual(self.aluno.notas["Matemática"], [8.0])

    def test_calcular_media(self):
        """Testa o cálculo da média das notas."""
        self.aluno.adicionar_nota("Matemática", 6.0)
        self.aluno.adicionar_nota("Matemática", 8.0)
        media = self.aluno.calcular_media("Matemática")
        self.assertEqual(media, 7.0)

    def test_calcular_media_sem_notas(self):
        """Testa a média de uma disciplina sem notas."""
        media = self.aluno.calcular_media("Português")
        self.assertEqual(media, 0.0)

    def test_registrar_falta(self):
        """Testa o registro de faltas em uma disciplina."""
        self.aluno.registrar_falta("Matemática")
        self.aluno.registrar_falta("Matemática")
        self.assertEqual(self.aluno.faltas["Matemática"], 2)

    def test_calcular_frequencia(self):
        """Testa o cálculo da frequência."""
        # 3 faltas em 20 aulas → 85%
        self.aluno.registrar_falta("História")
        self.aluno.registrar_falta("História")
        self.aluno.registrar_falta("História")
        frequencia = self.aluno.calcular_frequencia("História", 20)
        self.assertAlmostEqual(frequencia, 85.0)

    def test_calcular_frequencia_sem_faltas(self):
        """Testa a frequência quando não há faltas registradas."""
        frequencia = self.aluno.calcular_frequencia("Geografia", 10)
        self.assertEqual(frequencia, 100.0)

    def test_verificar_aprovacao_aprovado(self):
        """Testa aprovação com média >= 6.0 e frequência >= 75%."""
        self.aluno.adicionar_nota("Matemática", 7.0)
        self.aluno.adicionar_nota("Matemática", 9.0)
        # 2 faltas em 20 aulas = 90% frequência
        self.aluno.registrar_falta("Matemática")
        self.aluno.registrar_falta("Matemática")
        aprovado = self.aluno.verificar_aprovacao("Matemática", total_aulas=20)
        self.assertTrue(aprovado)

    def test_verificar_aprovacao_reprovado_por_media(self):
        """Testa reprovação por média baixa."""
        self.aluno.adicionar_nota("Física", 5.0)
        self.aluno.adicionar_nota("Física", 5.0)
        aprovado = self.aluno.verificar_aprovacao("Física", total_aulas=20)
        self.assertFalse(aprovado)

    def test_verificar_aprovacao_reprovado_por_frequencia(self):
        """Testa reprovação por frequência baixa."""
        self.aluno.adicionar_nota("Química", 9.0)
        self.aluno.adicionar_nota("Química", 9.0)
        for _ in range(6):  # 6 faltas em 20 aulas → 70%
            self.aluno.registrar_falta("Química")
        aprovado = self.aluno.verificar_aprovacao("Química", total_aulas=20)
        self.assertFalse(aprovado)


if __name__ == "__main__":
    unittest.main()
