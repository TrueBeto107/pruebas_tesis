from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class FechaPlantel(db.Model):
    __tablename__ = "fecha_plantel"

    id_fecha_plantel: Mapped[int] = mapped_column(primary_key=True)
    id_plantel: Mapped[str] = mapped_column(ForeignKey("plantel.abreviatura"))
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico")
    )
    fecha: Mapped[date] = mapped_column(Date)

    # Relaciones
    plantel: Mapped["Plantel"] = relationship(back_populates="fechas_plantel")
    evento_academico: Mapped["EventoAcademico"] = relationship(
        back_populates="fechas_plantel"
    )
