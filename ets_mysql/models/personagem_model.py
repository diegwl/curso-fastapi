from core.configs import settings
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship

from datetime import date

class PersonagemModel(settings.DBBaseModel):
    __tablename__ = "personagens"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    nacionalidade: int = Column(Integer)
    nascimento: date = Column(DATE)
    genero: str = Column(String(100))
    organizacao_id: int = Column(Integer, ForeignKey('organizacoes.id'))
    organizacao = relationship("OrganizacaoModel", back_populates='membros', lazy='joined')