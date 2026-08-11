from flask import render_template
from aplicacion.dto.documento_evento import CrearDocumentoDto
from aplicacion.dto.documento_evento import BuscarDocumentoDto
from aplicacion.servicio.evento import EventosServicio
from flask_jwt_extended import current_user
from aplicacion.dto.evento import BuscarEventosUsuarioDto


class EventosControlador:
    def __init__(self, servicio: EventosServicio):
        self.servicio = servicio

    def _buscar_todos_eventos(self):
        dto = BuscarEventosUsuarioDto(id_usuario=current_user.id_persona_academica)  
        return self.servicio.buscar_eventos(dto)

    def rederizar_eventos(self):
        eventos = self._buscar_todos_eventos()
        return render_template('eventos.html', lista_eventos=eventos)