from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from aplicacion.config import db


#No está completa
class Actividad(db.Model):
    __tablename__ = 'actividad'

    id_actividad: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200))
    descripcion: Mapped[str] = mapped_column(String(1500))

    documentos: Mapped[List["DocumentoEvento"]] = relationship(back_populates='actividad')