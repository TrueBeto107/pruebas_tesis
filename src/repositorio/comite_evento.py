from src.modelo.comite_evento import ComiteEvento
from src.interfaces.repositorio import ComiteEventoRepositorioI
from src.inicializacion.extenciones import db
from sqlalchemy import select
from sqlalchemy.orm import joinedload

class ComiteEventoRepositorio(ComiteEventoRepositorioI):
    
    def select_by_id_persona(self, id_persona: int) -> list[ComiteEvento]:
        #.options() sirve para establercer una estrategia para traer los objetos sin hacer un query mas
        stmt = select(ComiteEvento).where(ComiteEvento.id_persona == id_persona)#.options(joinedload(ComiteEvento.evento_academico))
        return list(db.session.scalars(stmt).all())