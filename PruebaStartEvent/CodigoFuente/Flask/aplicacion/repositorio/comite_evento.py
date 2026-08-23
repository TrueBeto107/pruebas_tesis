from aplicacion.modelo.comite_evento import ComiteEvento
from aplicacion.interfaces.repositorio import ComiteEventoRepositorioI
from aplicacion.inicializacion.extenciones import db
from sqlalchemy import select
from sqlalchemy.orm import joinedload

class ComiteEventoRepositorio(ComiteEventoRepositorioI):
    
    def select_by_id_persona(self, id_persona: int) -> list[ComiteEvento]:
        stmt = select(ComiteEvento).where(ComiteEvento.id_persona == id_persona)#.options(joinedload(ComiteEvento.evento_academico))
        return list(db.session.scalars(stmt).all())