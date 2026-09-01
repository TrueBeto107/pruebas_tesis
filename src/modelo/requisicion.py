from datetime import date

from sqlalchemy import CHAR, Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import TipoRequisicion
from src.inicializacion.extenciones import db


class Requisicion(db.Model):
    __tablename__ = "requisicion"

    id_requisicion: Mapped[int] = mapped_column(primary_key=True)
    id_evento_academico: Mapped[int] = mapped_column(
        ForeignKey("evento_academico.id_evento_academico")
    )
    id_plantel: Mapped[str] = mapped_column(ForeignKey("plantel.abreviatura"))
    numero_requisicion: Mapped[str] = mapped_column(CHAR(10))
    partida: Mapped[str] = mapped_column(String(10))
    tipo_requisicion: Mapped[TipoRequisicion]
    descripcion: Mapped[str] = mapped_column(String(1500))
    fecha_compra: Mapped[date] = mapped_column(Date)
    unidades_compradas: Mapped[int] = mapped_column(Integer)
    importe_comprado: Mapped[float] = mapped_column(Numeric(5, 2))
    ruta_requisicion: Mapped[str] = mapped_column(String(200))
    ruta_factura: Mapped[str] = mapped_column(String(200))

    # Relaciones
    evento_academico: Mapped["EventoAcademico"] = relationship(
        back_populates="requisiciones"
    )
    plantel: Mapped["Plantel"] = relationship(back_populates="requisiciones")
