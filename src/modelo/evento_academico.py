from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class EventoAcademico(db.Model):
    __tablename__ = "evento_academico"

    id_evento_academico: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200))
    edicion: Mapped[int] = mapped_column(Integer)
    tematica: Mapped[str] = mapped_column(String(200))
    presentacion: Mapped[str] = mapped_column(String(1000))

    temas: Mapped[list["TemaEvento"]] = relationship(back_populates="evento_academico")
    documentos: Mapped[list["DocumentoEvento"]] = relationship(
        "DocumentoEvento", back_populates="evento_academico"
    )
    comite_evento: Mapped["ComiteEvento"] = relationship(
        "ComiteEvento", back_populates="evento_academico"
    )
