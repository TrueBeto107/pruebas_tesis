from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm  import mapped_column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from aplicacion.inicializacion.extenciones import db

class EventoAcademico(db.Model):
    __tablename__ = "evento_academico"
    
    id_evento_academico: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200))
    edicion: Mapped[int] = mapped_column(Integer)
    tematica: Mapped[str] = mapped_column(String(200))
    presentacion: Mapped[str] = mapped_column(String(1000))

    #                    Objeto que se referencia                   Atributo que se referencia (en la otra tabla)
    temas: Mapped[List["TemaEvento"]] = relationship(back_populates='evento_academico')
    documentos: Mapped[List["DocumentoEvento"]] = relationship("DocumentoEvento",  back_populates='evento_academico')