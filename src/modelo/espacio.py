from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Espacio(db.Model):
    __tablename__ = "espacio"

    id_espacio: Mapped[int] = mapped_column(primary_key=True)
    id_plantel: Mapped[str] = mapped_column(ForeignKey("plantel.abreviatura"))
    ubicacion: Mapped[str] = mapped_column(String(50))
    es_principal: Mapped[bool] = mapped_column(Boolean)

    # Relaciones
    plantel: Mapped["Plantel"] = relationship(back_populates="espacios")


    fechas_espacio: Mapped[list["FechaEspacio"]] = relationship(
        back_populates="espacio"
    )
    horarios_actividad: Mapped[list["HorarioActividad"]] = relationship(
        back_populates="espacio"
    )
