from datetime import date, time

from sqlalchemy import Date, ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class ConvocatoriaActividad(db.Model):
    __tablename__ = "convocatoria_actividad"

    id_convocatoria_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(ForeignKey("actividad.id_actividad"), unique=True)
    fecha_expiracion: Mapped[date] = mapped_column(Date)
    hora_expiracion: Mapped[time] = mapped_column(Time)

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(
        back_populates="convocatorias_actividad"
        )
