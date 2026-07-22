
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm  import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from aplicacion.config import db

# No está completa
class PersonaAcademica(db.Model):
    __tablename__ = 'persona_academica'

    id_persona_academica: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))

    automovil: Mapped["Automovil"] = relationship(back_populates='persona')
    documentos: Mapped[List["DocumentoEvento"]] = relationship(back_populates='persona')