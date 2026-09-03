from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Agenda(db.Model):
    __tablename__ = "agenda"

    id_agenda: Mapped[int] = mapped_column(primary_key=True)
    id_plantel: Mapped[str] = mapped_column(ForeignKey("plantel.abreviatura"))
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad")
    )
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico")
    )

    # Relaciones
    plantel: Mapped["Plantel"] = relationship(back_populates="agendas")
    actividad: Mapped["Actividad"] = relationship(back_populates="agendas")
    evento_academico: Mapped["EventoAcademico"] = relationship(
        back_populates="agendas"
    )
