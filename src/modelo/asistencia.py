from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Asistencia(db.Model):
    __tablename__ = "asistente"

    id_asistencia: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(ForeignKey("actividad.id_actividad"))
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica")
    )
    fecha: Mapped[date | None] = mapped_column(Date, nullable=True)

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(back_populates="asistencias")
    persona_academica: Mapped["PersonaAcademica"] = relationship(back_populates="asistencias")
