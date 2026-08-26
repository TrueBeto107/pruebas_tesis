from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


# No está completa
class PersonaAcademica(db.Model):
    __tablename__ = "persona_academica"

    id_persona_academica: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    correo: Mapped[str] = mapped_column(String(255))
    contrasenia: Mapped[str] = mapped_column(String(255))
    es_administrador: Mapped[bool] = mapped_column(Boolean)
    sal: Mapped[str] = mapped_column(String(255))

    automovil: Mapped["Automovil"] = relationship(back_populates="persona")
    documentos: Mapped[list["DocumentoEvento"]] = relationship(back_populates="persona")
    comites_evento: Mapped[list["ComiteEvento"]] = relationship(
        back_populates="persona"
    )
