from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoParticipante
from src.inicializacion.extenciones import db


class Participante(db.Model):
    __tablename__ = "participante"

    id_participante: Mapped[int] = mapped_column(primary_key=True)
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad")
    )
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica")
    )
    tipo_participante: Mapped[TipoParticipante]

    # Relaciones
    actividad: Mapped["Actividad"] = relationship(
        back_populates="participantes"
    )
    persona_academica: Mapped["PersonaAcademica"] = relationship(
        back_populates="participantes"
    )
