from typing import Optional
from pydantic import BaseModel

class Personagens(BaseModel):
    id: Optional[int] = None
    nome: str
    apelido:str
    tipo:str
    caracteristicas:str
    img:str
    