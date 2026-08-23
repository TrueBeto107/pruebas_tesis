from flask import Blueprint, current_app as app
from aplicacion.servicio.evento import EventosServicio
from aplicacion.controlador.evento import EventosControlador

from flask_jwt_extended import jwt_required

def crear_evento_blueprint(controlador: EventosControlador):
    evento_academico_bp = Blueprint(
        'eventos',
        __name__,
        url_prefix='/eventos',
        template_folder=app.config['DIRECTORIO_TEMPLATES'] / 'eventos'
        )

    @evento_academico_bp.route('/')
    @jwt_required()
    def mostrar_eventos_asociados():
        return controlador.rederizar_eventos()

    @evento_academico_bp.route('/modal')
    def mostrar_modal_evento():
        return controlador.renderizar_modal_evento()

    @evento_academico_bp.route('/quitar_modal')
    def esconder_modal_evento():
        return controlador.renderizar_modal_vacia()

    return evento_academico_bp