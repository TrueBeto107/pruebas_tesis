
from sqlalchemy.orm import Mapped
from sqlalchemy.orm  import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from src.inicializacion.extenciones import db


class TemaEvento(db.Model):
    __tablename__ = 'tema_evento'

    id_tema_evento: Mapped[int] = mapped_column(primary_key=True)
    id_evento: Mapped[int] = mapped_column(ForeignKey('evento_academico.id_evento_academico'))
    tema: Mapped[str] = mapped_column(String(50))

    #Atributo referenciado
    evento_academico: Mapped["EventoAcademico"] = relationship(back_populates='temas')