from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import CarrerasUACM, EstadoActividad
from src.inicializacion.extenciones import db


class Actividad(db.Model):
    __tablename__ = "actividad"

    id_actividad: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200))
    descripcion: Mapped[str] = mapped_column(String(1500))
    carrera_asociada: Mapped[CarrerasUACM | None]
    estado_actividad: Mapped[EstadoActividad]
    numero_dias: Mapped[int] = mapped_column(SmallInteger)
    link_reunion: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )
    token: Mapped[str] = mapped_column(String(64))

    # Relaciones
    agendas: Mapped[list["Agenda"]] = relationship(back_populates="actividad")
    actividades_compartidas: Mapped[list["ActividadCompartida"]] = (
        relationship(back_populates="actividad")
    )
    asistencias: Mapped[list["Asistencia"]] = relationship(
        back_populates="actividad"
    )
    horarios_actividad: Mapped[list["HorarioActividad"]] = relationship(
        back_populates="actividad"
    )
    documentos_evento: Mapped[list["DocumentoEvento"]] = relationship(
        back_populates="actividad"
    )
    participantes: Mapped[list["Participante"]] = relationship(
        back_populates="actividad"
    )
    convocatorias_actividad: Mapped[list["ConvocatoriaActividad"]] = (
        relationship(back_populates="actividad")
    )
    fechas_preferenciales: Mapped[list["FechaPreferencial"]] = relationship(
        back_populates="actividad"
    )
    palabras_clave_actividad: Mapped[list["PalabraClaveActividad"]] = (
        relationship(back_populates="actividad")
    )
    propiedades_actividad: Mapped["PropiedadesActividad"] = relationship(
        back_populates="actividad"
    )
