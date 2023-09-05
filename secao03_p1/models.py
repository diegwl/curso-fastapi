from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 2:
            raise ValueError('O título deve ter pelo menos 2 palavras.')

        if value.islower():
            raise ValueError('O título precisa ser capitalizado.')

        return value

cursos = [
    Curso(id=0, titulo='Programação para Leigos', aulas=42, horas=56),
    Curso(id=1, titulo='Algoritmos e Lógica de Programação', aulas=52, horas=66),
]