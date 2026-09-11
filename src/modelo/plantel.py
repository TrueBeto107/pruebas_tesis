from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Plantel(db.Model):
    __tablename__ = "plantel"

    abreviatura: Mapped[str] = mapped_column(String(5), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    correo_contacto: Mapped[str] = mapped_column(String(255))
    direccion: Mapped[str] = mapped_column(String(150))

    # Relaciones
    documentos_evento: Mapped[list["DocumentoEvento"]] = relationship(
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    comites_evento: Mapped[list["ComiteEvento"]] = relationship(
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    actividades_compartidas: Mapped[list["ActividadCompartida"]] = (
        relationship(
            back_populates="plantel_destinatario",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    autoridades: Mapped[list["Autoridad"]] = relationship(
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    espacios: Mapped[list["Espacio"]] = relationship(
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    agendas: Mapped[list["Agenda"]] = relationship(
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    fechas_plantel: Mapped[list["FechaPlantel"]] = relationship(
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    requisiciones: Mapped[list["Requisicion"]] = relationship(
        back_populates="plantel",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
