from datetime import date, time

from sqlalchemy import Date, ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class HorarioActividad(db.Model):
    __tablename__ = "horario_actividad"

    id_horario_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int | None]  = mapped_column(
        ForeignKey("actividad.id_actividad"), nullable=True
    )
    id_espacio: Mapped[int] = mapped_column(ForeignKey("espacio.id_espacio"))
    fecha: Mapped[date] = mapped_column(Date)
    hora_inicio: Mapped[time] = mapped_column(Time)
    hora_fin: Mapped[time | None] = mapped_column(Time, nullable=True)

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(back_populates="horarios_actividad")
    espacio: Mapped["Espacio"] = relationship(back_populates="horarios_actividad")
