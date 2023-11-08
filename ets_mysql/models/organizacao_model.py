from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings


class OrganizacaoModel(settings.DBBaseModel):
    __tablename__ = 'organizacoes'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    localidade: str = Column(String(100))
    membros = relationship(
        "PersonagemModel",
        cascade="all,delete-orphan",
        back_populates="organizacao",
        uselist=True,
        lazy="joined"
    )