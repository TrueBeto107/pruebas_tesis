from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoActividad
from src.inicializacion.extenciones import db


class PropiedadesActividad(db.Model):
    __tablename__ = "propiedades_actividad"

    id_propiedades_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad"), unique=True
    )
    tipo_actividad: Mapped[TipoActividad]
    documentacion: Mapped[str | None] = mapped_column(
        String(200), nullable=True
    )
    cartel_promocional: Mapped[str | None] = mapped_column(
        String(200), nullable=True
    )
    cupo_maximo: Mapped[int | None] = mapped_column(
        SmallInteger, nullable=True
    )
    referencias: Mapped[str | None] = mapped_column(
        String(5000), nullable=True
    )

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(
        back_populates="propiedades_actividad"
    )
