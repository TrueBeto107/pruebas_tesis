from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import CarrerasUACM, EstadoActividad
from src.inicializacion.extenciones import db


class Actividad(db.Model):
    __tablename__ = "actividad"

    id_actividad: Mapped[int] = mapped_column(primary_key=True)
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico", ondelete="CASCADE")
    )
    titulo: Mapped[str] = mapped_column(String(200))
    descripcion: Mapped[str] = mapped_column(String(1500))
    carrera_asociada: Mapped[CarrerasUACM | None]
    estado_actividad: Mapped[EstadoActividad]
    numero_dias: Mapped[int] = mapped_column(SmallInteger)
    link_reunion: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )
    token: Mapped[str] = mapped_column(String(64), nullable=True)

    # Relaciones
    evento_academico: Mapped["EventoAcademico"] = relationship(
        back_populates="actividades"
    )
    agendas: Mapped[list["Agenda"]] = relationship(
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    actividades_compartidas: Mapped[list["ActividadCompartida"]] = (
        relationship(
            back_populates="actividad",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    asistencias: Mapped[list["Asistencia"]] = relationship(
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    horarios_actividad: Mapped[list["HorarioActividad"]] = relationship(
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    documentos_evento: Mapped[list["DocumentoEvento"]] = relationship(
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    participantes: Mapped[list["Participante"]] = relationship(
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    convocatorias_actividad: Mapped[list["ConvocatoriaActividad"]] = (
        relationship(
            back_populates="actividad",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    fechas_preferenciales: Mapped[list["FechaPreferencial"]] = relationship(
        back_populates="actividad",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    palabras_clave_actividad: Mapped[list["PalabraClaveActividad"]] = (
        relationship(
            back_populates="actividad",
            cascade="all, delete-orphan",
            passive_deletes=True,
        )
    )
    propiedades_actividad: Mapped["PropiedadesActividad"] = relationship(
        back_populates="actividad"
    )
