from core.configs import settings

from sqlalchemy.orm import Mapped

from sqlalchemy import Column, Integer, String


class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = Column(String(100))
    aulas: Mapped[int] = Column(Integer)
    horas: Mapped[int] = Column(Integer)