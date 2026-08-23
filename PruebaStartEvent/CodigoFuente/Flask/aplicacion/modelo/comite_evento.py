from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from aplicacion.enums import AccesoOrganizador
from aplicacion.inicializacion.extenciones import db 
  
class ComiteEvento(db.Model):
    __tablename__ = "comite_evento"

    #Columnas
    id_comite_evento: Mapped[int] = mapped_column(primary_key=True)
    id_plantel: Mapped[str] = mapped_column(ForeignKey("plantel.abreviatura"))
    id_evento_academico: Mapped[int] = mapped_column(ForeignKey("evento_academico.id_evento_academico"))
    id_persona: Mapped[int] = mapped_column(ForeignKey("persona_academica.id_persona_academica"))
    acceso_organizador: Mapped[AccesoOrganizador]

    #Relaciones
    plantel: Mapped["Plantel"] = relationship(back_populates="comites_evento")
    evento_academico: Mapped["EventoAcademico"] = relationship(back_populates="comite_evento")
    persona: Mapped["PersonaAcademica"] = relationship(back_populates="comites_evento")