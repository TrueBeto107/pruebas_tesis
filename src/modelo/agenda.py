from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.inicializacion.extenciones import db


class Agenda(db.Model):
    __tablename__ = "agenda"

    id_agenda: Mapped[int] = mapped_column(primary_key=True)
    id_plantel: Mapped[str] = mapped_column(
        ForeignKey("plantel.abreviatura", ondelete="CASCADE")
    )
    id_actividad: Mapped[int] = mapped_column(
        ForeignKey("actividad.id_actividad", ondelete="CASCADE")
    )

    # Relaciones
    plantel: Mapped["Plantel"] = relationship(back_populates="agendas")
    actividad: Mapped["Actividad"] = relationship(back_populates="agendas")
