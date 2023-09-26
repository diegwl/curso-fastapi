from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, Mapped

from core.configs import settings

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'
    
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = Column(String(256), nullable=True)
    sobrenome: Mapped[str] = Column(String(256), nullable=True)
    email: Mapped[str] = Column(String(256), index=True, nullable=False, unique=True)
    senha: Mapped[str] = Column(String(256), nullable=False)
    eh_admin: Mapped[bool] = Column(Boolean, default=False)
    artigos = relationship(
        "ArtigoModel",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )
    