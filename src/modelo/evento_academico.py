from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class EventoAcademico(db.Model):
    __tablename__ = "evento_academico"

    id_evento_academico: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200))
    edicion: Mapped[int] = mapped_column(SmallInteger)
    tematica: Mapped[str | None] = mapped_column(String(200), nullable=True)
    presentacion: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    # Relaciones
    temas_evento: Mapped[list["TemaEvento"]] = relationship(back_populates="evento_academico")
    documentos_evento: Mapped[list["DocumentoEvento"]] = relationship(
        "DocumentoEvento", back_populates="evento_academico"
    )
    comites_evento: Mapped[list["ComiteEvento"]] = relationship(
        "ComiteEvento", back_populates="evento_academico"
    )
    agendas : Mapped[list["Agenda"]] = relationship(back_populates="evento_academico")
    requisiciones: Mapped[list["Requisicion"]] = relationship(back_populates="evento_academico")
    colores_evento: Mapped[list["ColorEvento"]] = relationship(
        back_populates="evento_academico"
    )
    fechas_plantel: Mapped[list["FechaPlantel"]] = relationship(
        back_populates="evento_academico"
    )
    