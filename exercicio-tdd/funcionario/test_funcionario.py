"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        funcionario = Funcionario(
            nome="João",
            matricula=1,
            salario_hora=50.0,
            horas_trabalhadas=160  # 160 horas no mês
        )
        salario_esperado = 50.0 * 160
        self.assertEqual(funcionario.calcular_salario_bruto(), salario_esperado)

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        funcionario = Funcionario(
            nome="Maria",
            matricula=2,
            salario_hora=50.0,
            horas_trabalhadas=160,
            custo_empregador=1000.0,
            tem_comissao=True,
            valor_comissao=200.0,
            contratos_fechados=3
        )
        salario_bruto = 50.0 * 160
        comissao = 200.0 * 3
        custo_total_esperado = salario_bruto + 1000.0 + comissao
        self.assertEqual(funcionario.calcular_custo_total(), custo_total_esperado)

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        funcionario = Funcionario(
            nome="Carlos",
            matricula=3,
            salario_hora=60.0,
            horas_trabalhadas=150,
            tem_comissao=True,
            valor_comissao=150.0,
            contratos_fechados=4
        )
        comissao_esperada = 150.0 * 4
        self.assertEqual(funcionario.calcular_comissao(), comissao_esperada)

        # Também vamos testar o caso de funcionário sem comissão:
        funcionario_sem_comissao = Funcionario(
            nome="Ana",
            matricula=4,
            salario_hora=60.0,
            horas_trabalhadas=150,
            tem_comissao=False,  # <- não tem comissão
            valor_comissao=150.0,  # mesmo que tenha valor, não deve contar
            contratos_fechados=4
        )
        self.assertEqual(funcionario_sem_comissao.calcular_comissao(), 0.0)


if __name__ == "__main__":
    unittest.main()
