"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta

from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.produto = Produto(
            codigo="001",
            nome="Sabonete",
            preco=5.0,
            quantidade=20,
            estoque_minimo=10,
            data_validade=datetime.now() + timedelta(days=10)  # produto válido
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.codigo, "001")
        self.assertEqual(self.produto.nome, "Sabonete")
        self.assertEqual(self.produto.preco, 5.0)
        self.assertEqual(self.produto.quantidade, 20)
        self.assertEqual(self.produto.estoque_minimo, 10)
        self.assertTrue(isinstance(self.produto.data_validade, datetime))

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.quantidade, 30)

        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-5)  # Quantidade inválida

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        sucesso = self.produto.remover_estoque(5)
        self.assertTrue(sucesso)
        self.assertEqual(self.produto.quantidade, 15)

        falha = self.produto.remover_estoque(100)
        self.assertFalse(falha)  # Não pode remover mais do que há em estoque
        self.assertEqual(self.produto.quantidade, 15)

        with self.assertRaises(ValueError):
            self.produto.remover_estoque(-3)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.assertFalse(self.produto.verificar_estoque_baixo())

        self.produto.quantidade = 5
        self.assertTrue(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        valor_total = self.produto.calcular_valor_total()
        self.assertEqual(valor_total, 5.0 * 20)

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        self.assertTrue(self.produto.verificar_validade())

        vencido = Produto(
            codigo="002",
            nome="Shampoo",
            preco=10.0,
            quantidade=10,
            data_validade=datetime.now() - timedelta(days=1)  # vencido
        )
        self.assertFalse(vencido.verificar_validade())

        sem_validade = Produto(
            codigo="003",
            nome="Escova",
            preco=3.0,
            quantidade=5,
            data_validade=None
        )
        self.assertTrue(sem_validade.verificar_validade())


if __name__ == "__main__":
    unittest.main()
