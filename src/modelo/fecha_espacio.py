from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class FechaEspacio(db.Model):
    __tablename__ = "fecha_espacio"

    id_fecha_espacio: Mapped[int] = mapped_column(primary_key=True)
    id_espacio: Mapped[int] = mapped_column(ForeignKey("espacio.id_espacio"))
    fecha: Mapped[date] = mapped_column(Date)

    # Relaciones
    espacio: Mapped["Espacio"] = relationship(back_populates="fechas_espacio")
