"""
Sistema de gerenciamento de notas escolares.
"""
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Aluno:
    nome: str
    matricula: str
    notas: Dict[str, List[float]] = None  # Disciplina -> Lista de notas
    faltas: Dict[str, int] = None  # Disciplina -> Número de faltas

    def __post_init__(self):
        if self.notas is None:
            self.notas = {}
        if self.faltas is None:
            self.faltas = {}

    def adicionar_nota(self, disciplina: str, nota: float) -> None:
        if disciplina not in self.notas:
            self.notas[disciplina] = []
        self.notas[disciplina].append(nota)

    def calcular_media(self, disciplina: str) -> float:
        notas = self.notas.get(disciplina, [])
        if not notas:
            return 0.0
        return sum(notas) / len(notas)

    def verificar_aprovacao(self, disciplina: str, total_aulas: int = 100) -> bool:
        media = self.calcular_media(disciplina)
        frequencia = self.calcular_frequencia(disciplina, total_aulas)
        return media >= 6.0 and frequencia >= 75.0

    def registrar_falta(self, disciplina: str) -> None:
        if disciplina not in self.faltas:
            self.faltas[disciplina] = 0
        self.faltas[disciplina] += 1

    def calcular_frequencia(self, disciplina: str, total_aulas: int) -> float:
        faltas = self.faltas.get(disciplina, 0)
        if total_aulas <= 0:
            return 0.0
        presencas = total_aulas - faltas
        return (presencas / total_aulas) * 100
