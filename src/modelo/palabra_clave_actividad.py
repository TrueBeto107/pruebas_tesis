from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class PalabraClaveActividad(db.Model):
    __tablename__ = "palabra_clave_actividad"

    id_palabra_clave_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad")
    )
    palabra_clave: Mapped[str] = mapped_column(String(30))

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(
        back_populates="palabras_clave_actividad"
    )
