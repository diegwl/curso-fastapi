from typing import Optional

from pydantic import BaseModel, HttpUrl

class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: str
    usuario_id: Optional[int] = None
    
    class Config:
        orm_mode = True