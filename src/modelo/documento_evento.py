from datetime import date, time

from sqlalchemy import Date, ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import SubtipoDocumento, TipoDocumento
from src.inicializacion.extenciones import db


class DocumentoEvento(db.Model):
    __tablename__ = "documento_evento"

    id_documento_evento: Mapped[int] = mapped_column(primary_key=True)
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico")
    )
    id_plantel: Mapped[str | None] = mapped_column(
        ForeignKey("plantel.abreviatura"), nullable=True
    )
    id_persona_academica: Mapped[int | None] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica"), nullable=True
    )
    id_actividad: Mapped[int | None] = mapped_column(
        ForeignKey("actividad.id_actividad"), nullable=True
    )
    fecha_expiracion: Mapped[date | None] = mapped_column(Date, nullable=True)
    hora_expiracion: Mapped[time | None] = mapped_column(Time, nullable=True)
    tipo_documento: Mapped[TipoDocumento]
    subtipo_documento: Mapped[SubtipoDocumento]
    ruta_archivo: Mapped[str] = mapped_column(String(200))

    # Relaciones
    evento_academico: Mapped["EventoAcademico"] = relationship(
        back_populates="documentos_evento"
    )
    plantel: Mapped["Plantel"] = relationship(back_populates="documentos_evento")
    persona_academica: Mapped["PersonaAcademica"] = relationship(back_populates="documentos_evento")
    actividad: Mapped["Actividad"] = relationship(back_populates="documentos_evento")
   
