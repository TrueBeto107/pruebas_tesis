from aplicacion.modelo.comite_evento import ComiteEvento
from aplicacion.inicializacion.extenciones import db

class ComiteEventoRepositorio:
   
    def select_by_persona_id(self, persona_id: int) -> list:
        return ComiteEvento.query.filter_by(id_persona=persona_id).all()