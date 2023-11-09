from typing import Optional

from datetime import date

from pydantic import BaseModel as SchemaBaseModel

class PersonagemSchema(SchemaBaseModel):
    id: Optional[int] = None
    nome: str
    nacionalidade: str
    nascimento: date
    genero: str
    organizacao_id: Optional[int] = None

    class Config:
        from_attributes=True