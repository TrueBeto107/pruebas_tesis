from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoTelefono
from src.inicializacion.extenciones import db


class TelefonoPersona(db.Model):
    __tablename__ = "telefono_persona"

    id_telefono_persona: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica")
    )
    tipo_telefono: Mapped[TipoTelefono]
    numero_telefono: Mapped[str] = mapped_column(String(25))
    extension: Mapped[str] = mapped_column(String(10))

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(back_populates="telefonos_persona")
