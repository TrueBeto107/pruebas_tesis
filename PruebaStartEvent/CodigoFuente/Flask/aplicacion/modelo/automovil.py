from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from aplicacion.inicializacion.extenciones import db

class Automovil(db.Model):
    __tablename__ = 'automovil'

    id_automovil: Mapped[int] = mapped_column(primary_key=True)
    id_persona_academica: Mapped[int] = mapped_column(ForeignKey('persona_academica.id_persona_academica'), unique=True)
    placa: Mapped[str] = mapped_column(String(10))
    modelo: Mapped[str] = mapped_column(String(50))
    anio: Mapped[str] = mapped_column(String(4))
    color: Mapped[str] = mapped_column(String(20))

    persona: Mapped["PersonaAcademica"] = relationship(back_populates='automovil')