from sqlalchemy import CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoColor
from src.inicializacion.extenciones import db


class ColorEvento(db.Model):
    __tablename__ = "color_evento"

    id_color_evento: Mapped[int] = mapped_column(primary_key=True)
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico")
    )
    tipo_color: Mapped[TipoColor]
    codigo_hexadecimal: Mapped[str] = mapped_column(CHAR(8))

    # Relaciones
    evento_academico: Mapped["EventoAcademico"] = relationship(
        back_populates="colores_evento"
    )
