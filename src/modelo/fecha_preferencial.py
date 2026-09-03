from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class FechaPreferencial(db.Model):
    __tablename__ = "fecha_preferencial"

    id_fecha_preferencial: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad")
    )
    fecha: Mapped[date] = mapped_column(Date)

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(
        back_populates="fechas_preferenciales"
    )
