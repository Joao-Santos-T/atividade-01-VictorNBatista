"""
Sistema de gerenciamento de funcionários.

Este módulo implementa a classe Funcionario que representa um funcionário
com foco em cálculos trabalhistas e comissões. A classe permite calcular
salário bruto, custos totais e comissões de forma flexível e segura.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Funcionario:
    """Representação de um funcionário com foco em custos trabalhistas e comissões.
    
    Esta classe implementa cálculos trabalhistas básicos incluindo:
    - Cálculo de salário bruto baseado em horas trabalhadas
    - Cálculo de custos totais incluindo encargos trabalhistas
    - Cálculo de comissões baseado em contratos fechados
    
    Attributes:
        nome: Nome do funcionário
        matricula: Número de matrícula do funcionário
        salario_hora: Valor do salário por hora trabalhada (deve ser positivo)
        horas_trabalhadas: Quantidade de horas trabalhadas no mês (deve ser positiva)
        custo_empregador: Custo fixo mensal do empregador (INSS, FGTS, etc) (deve ser positivo)
        tem_comissao: Indica se o funcionário recebe comissão
        valor_comissao: Valor da comissão por contrato fechado (deve ser positivo se tem_comissao=True)
        contratos_fechados: Número de contratos fechados no mês (deve ser não negativo)
    """

    nome: str
    matricula: int
    salario_hora: float = 100.0
    horas_trabalhadas: float = 0.0
    custo_empregador: float = 1000.0
    tem_comissao: bool = True
    valor_comissao: float = 100.0
    contratos_fechados: int = 0

    def __post_init__(self) -> None:
        """Valida os atributos após a inicialização.
        
        Raises:
            ValueError: Se algum dos valores numéricos for inválido
        """
        if self.salario_hora <= 0:
            raise ValueError("Salário por hora deve ser positivo")
        if self.horas_trabalhadas < 0:
            raise ValueError("Horas trabalhadas não podem ser negativas")
        if self.custo_empregador < 0:
            raise ValueError("Custo do empregador não pode ser negativo")
        if self.tem_comissao and self.valor_comissao <= 0:
            raise ValueError("Valor da comissão deve ser positivo quando tem_comissao=True")
        if self.contratos_fechados < 0:
            raise ValueError("Número de contratos fechados não pode ser negativo")

    def calcular_salario_bruto(self) -> float:
        """Calcula o salário bruto do funcionário.
        
        O salário bruto é calculado multiplicando o salário por hora
        pelo número de horas trabalhadas.
        
        Returns:
            float: Salário bruto calculado baseado nas horas trabalhadas
        """
        return self.salario_hora * self.horas_trabalhadas

    def calcular_custo_total(self) -> float:
        """Calcula o custo total do funcionário para a empresa.
        
        O custo total inclui:
        - Salário bruto
        - Custo fixo do empregador (INSS, FGTS, etc)
        - Comissões (se aplicável)
        
        Returns:
            float: Custo total (salário + custos do empregador + comissão)
        """
        return self.calcular_salario_bruto() + self.custo_empregador + self.calcular_comissao()

    def calcular_comissao(self) -> float:
        """Calcula o valor total da comissão do funcionário.
        
        A comissão é calculada multiplicando o valor da comissão por contrato
        pelo número de contratos fechados. Se o funcionário não tem direito
        a comissão, retorna 0.
        
        Returns:
            float: Valor total da comissão baseado nos contratos fechados
        """
        if not self.tem_comissao:
            return 0.0
        return self.valor_comissao * self.contratos_fechados 