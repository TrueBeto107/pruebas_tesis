from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class ActividadCompartida(db.Model):
    __tablename__ = "actividad_compartida"

    id_actividad_compartida: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(ForeignKey("actividad.id_actividad"))
    id_remitente: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica")
    )
    id_destinatario: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica")
    )
    id_plantel_destinatario: Mapped[str] = mapped_column(
        ForeignKey("plantel.abreviatura")
    )

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(
        back_populates="actividades_compartidas"
    )
    remitente: Mapped["PersonaAcademica"] = relationship(
        foreign_keys=[id_remitente], back_populates="actividades_compartidas_remitente"
    )
    destinatario: Mapped["PersonaAcademica"] = relationship(
        foreign_keys=[id_destinatario],
        back_populates="actividades_compartidas_destinatario",
    )
    plantel_destinatario: Mapped["Plantel"] = relationship(
        back_populates="actividades_compartidas"
    )
