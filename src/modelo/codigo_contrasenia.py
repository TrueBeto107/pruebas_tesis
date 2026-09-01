from datetime import date, time

from sqlalchemy import Boolean, Date, ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class CodigoContrasenia(db.Model):
    __tablename__ = "codigo_contrasenia"

    id_codigo_contrasenia: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica")
    )
    codigo_hash: Mapped[str] = mapped_column(String(64))  # Verificar longitud
    fecha_expiracion: Mapped[date] = mapped_column(Date)
    hora_expiracion: Mapped[time] = mapped_column(Time)
    usado: Mapped[bool] = mapped_column(Boolean)

    # Relaciones
    persona_academica: Mapped["PersonaAcademica"] = relationship(
        back_populates="codigos_contrasenia"
    )
