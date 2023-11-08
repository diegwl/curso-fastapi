from typing import Optional, List

from pydantic import BaseModel as SchemaBaseModel

from schemas.personagem_schema import PersonagemSchema

class OrganizacaoSchemaBase(SchemaBaseModel):
    id: Optional[int] = None
    nome: str
    localidade: str

    class Config:
        from_attributes=True

class OrganizacaoSchemaMembros(OrganizacaoSchemaBase):
    membros: Optional[List[PersonagemSchema]]