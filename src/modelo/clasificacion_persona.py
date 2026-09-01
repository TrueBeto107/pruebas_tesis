from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import SubtipoPersona, TipoPersona
from src.inicializacion.extenciones import db


class ClasificacionPersona(db.Model):
    __tablename__ = "clasificacion_persona"

    id_clasificacion_persona: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica")
    )
    tipo_persona: Mapped[TipoPersona]
    subtipo_persona: Mapped[SubtipoPersona]

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(
        back_populates="clasificaciones_persona"
    )
