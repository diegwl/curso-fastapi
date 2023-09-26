from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from core.configs import settings

class ArtigoModel(settings.DBBaseModel):
    __tablename__ = 'artigos'
    
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = Column(String(256))
    url_fonte: Mapped[str] = Column(String(256))
    descricao: Mapped[str] = Column(String(256))
    usuario_id: Mapped[int] = Column(Integer, ForeignKey('usuarios.id'))
    criador = relationship("UsuarioModel", back_populates='artigos', lazy='joined')
