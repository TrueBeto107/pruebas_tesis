
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm  import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from aplicacion.inicializacion.extenciones import db

class Plantel(db.Model):
    __tablename__ = 'plantel'

    abreviatura: Mapped[str] = mapped_column(String(5), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    correo_contacto: Mapped[str] = mapped_column(String(255))
    direccion: Mapped[str] = mapped_column(String(150))

    documentos: Mapped[List["DocumentoEvento"]] = relationship(back_populates='plantel')
    comites_evento: Mapped[List["ComiteEvento"]] = relationship(back_populates='plantel')