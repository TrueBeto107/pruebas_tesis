from aplicacion.modelo.evento_academico import EventoAcademico
from aplicacion.inicializacion.extenciones import db


class EventosRepositorio:
    
    def select_all(self) -> list:
        return EventoAcademico.query.all()
    
    def select_by_user_id(self, user_id: int) -> list:
        return EventoAcademico.query.filter_by(id_usuario=user_id).all()