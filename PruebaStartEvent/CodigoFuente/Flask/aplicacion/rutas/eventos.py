from flask import current_app as app
from flask import request
from aplicacion.servicio.evento import EventosServicio
from aplicacion.controlador.evento import EventosControlador

from flask_jwt_extended import jwt_required
import hashlib

controlador = EventosControlador(EventosServicio())

@app.route('/eventos')
@jwt_required()
def mostrar_eventos_asociados():
    return controlador.rederizar_eventos()

@app.route('/evento/modal')
def modal_evento():
    return controlador.renderizar_modal_evento()