from flask import render_template
from src.dto.persona_academica import MostrarInformacionUsuarioDto 
from src.servicio.evento import EventosServicio
from flask_jwt_extended import current_user
from src.dto.evento import BuscarEventosUsuarioDto


class EventosControlador:
    def __init__(self, servicio: EventosServicio):
        self.servicio = servicio

    def _buscar_todos_eventos(self):
        dto = BuscarEventosUsuarioDto(id_usuario=current_user.id_persona_academica)  
        return self.servicio.buscar_eventos(dto)

    def rederizar_eventos(self):
        eventos = self._buscar_todos_eventos()
        usuario = MostrarInformacionUsuarioDto(nombre_completo=current_user.nombre, es_administrador=current_user.es_administrador)
        return render_template('eventos.html', lista_eventos=eventos, usuario=usuario)
    
    def renderizar_modal_evento(self):
        modal = "Probando ventana modal"
        return render_template('modal.html',modal=modal)

    def renderizar_modal_vacia(self):
        return '<div id="div-modal" class="absolute left-0 top-0 z-20"></div>'