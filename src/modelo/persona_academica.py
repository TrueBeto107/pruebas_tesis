from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import EstadoActivo, NivelEstudios, TipoInstitucion
from src.inicializacion.extenciones import db


class PersonaAcademica(db.Model):
    __tablename__ = "persona_academica"

    id_persona_academica: Mapped[int] = mapped_column(primary_key=True)
    nombres: Mapped[str] = mapped_column(String(50))
    apellido_paterno: Mapped[str] = mapped_column(String(50))
    apellido_materno: Mapped[str | None] = mapped_column(String(50), nullable=True)
    correo_contacto: Mapped[str | None] = mapped_column(String(255), nullable=True)
    estado_activo: Mapped[EstadoActivo]
    contrasenia: Mapped[str | None] = mapped_column(
        String(64), nullable=True
    )  # Verificar longitud
    sal: Mapped[str | None] = mapped_column(
        String(64), nullable=True
    )  # Verificar longitud
    es_administrador: Mapped[bool | None]   = mapped_column(Boolean, nullable=True)
    cubiculo: Mapped[str | None] = mapped_column(String(10), nullable=True)
    ruta_foto_perfil: Mapped[str] = mapped_column(String(200))
    semblanza: Mapped[str | None] = mapped_column(String(1500), nullable=True)
    intereses: Mapped[str | None] = mapped_column(String(250), nullable=True)
    institucion_procedencia: Mapped[str | None] = mapped_column(
        String(200), nullable=True
    )
    tipo_institucion: Mapped[TipoInstitucion | None]
    nivel_estudios: Mapped[NivelEstudios | None]
    discapacidad: Mapped[str | None] = mapped_column(String(200), nullable=True)
    ruta_foto_ponente: Mapped[str | None] = mapped_column(String(200), nullable=True)

    # Relaciones
    telefonos_persona: Mapped[list["TelefonoPersona"]] = relationship(
        back_populates="persona"
    )
    autoridades: Mapped[list["Autoridad"]] = relationship(back_populates="persona_academica")
    comites_evento: Mapped[list["ComiteEvento"]] = relationship(
        back_populates="persona_academica"
    )
    documentos_evento: Mapped[list["DocumentoEvento"]] = relationship(back_populates="persona_academica")
    actividades_compartidas_remitente: Mapped[list["ActividadCompartida"]] = relationship(
        foreign_keys="[id_remitente]",
        back_populates="remitente",
    )
    actividades_compartidas_destinatario: Mapped[list["ActividadCompartida"]] = relationship(
        foreign_keys="[id_destinatario]",
        back_populates="destinatario",
    )
    asistencias: Mapped[list["Asistencia"]] = relationship(back_populates="persona_academica")
    automovil: Mapped["Automovil"] = relationship(back_populates="persona_academica")
    clasificaciones_persona: Mapped[list["ClasificacionPersona"]] = relationship(back_populates="persona_academica")
    codigos_contrasenia: Mapped[list["CodigoContrasenia"]] = relationship(back_populates="persona_academica")
    participantes: Mapped[list["Participante"]] = relationship(back_populates="persona_academica")