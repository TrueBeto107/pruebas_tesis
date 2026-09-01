from datetime import date

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoAutoridad
from src.inicializacion.extenciones import db


class Autoridad(db.Model):
    __tablename__ = "autoridad"

    id_autoridad: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica")
    )
    id_plantel: Mapped[str | None] = mapped_column(
        ForeignKey("plantel.abreviatura"), nullable=True
    )
    tipo_autoridad: Mapped[TipoAutoridad]
    fecha_ingreso: Mapped[date] = mapped_column(Date)
    fecha_egreso: Mapped[date | None]  = mapped_column(Date, nullable=True)

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(back_populates="autoridades")
    plantel: Mapped["Plantel"] = relationship(back_populates="autoridades")
