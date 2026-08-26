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
    id_plantel: Mapped[str] = mapped_column(
        ForeignKey("plantel.abreviatura"), nullable=True
    )
    id_persona: Mapped[int] = mapped_column(
        ForeignKey("persona_academica.id_persona_academica"), nullable=True
    )
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad"), nullable=True
    )
    fecha_expiracion: Mapped[Date] = mapped_column(Date, nullable=True)
    hora_expiracion: Mapped[Time] = mapped_column(Time, nullable=True)
    tipo_documento: Mapped[TipoDocumento]
    subtipo_documento: Mapped[SubtipoDocumento]
    ruta_archivo: Mapped[str] = mapped_column(String(50))

    evento_academico: Mapped["EventoAcademico"] = relationship(
        back_populates="documentos"
    )
    plantel: Mapped["Plantel"] = relationship(back_populates="documentos")
    persona: Mapped["PersonaAcademica"] = relationship(back_populates="documentos")
    actividad: Mapped["Actividad"] = relationship(back_populates="documentos")
