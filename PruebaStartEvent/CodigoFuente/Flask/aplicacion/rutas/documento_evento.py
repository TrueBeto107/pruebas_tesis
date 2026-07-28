from flask import current_app as app
from flask import request
from aplicacion.servicio.documento_evento import DocumentoEventoServicio
from aplicacion.controlador.documento_evento import DocumentoControlador

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt
import hashlib

controlador = DocumentoControlador(DocumentoEventoServicio())

@app.route('/documento')
@jwt_required()
def gestion_documentos():
    #id = get_jwt_identity()
    claims = get_jwt()
    nombre = claims['nombre']
    
    return controlador.rederizar_gestion_documentos(nombre)

@app.route('/tabla')
def actualizar_tabla():
    return controlador.renderizar_tabla()

@app.route('/mostrar/<ruta>')
def mostrar(ruta):
    return controlador.renderizar_documento(ruta)

@app.get('/documento/buscar')
def get_documento():
    id = request.args.get('id_documento')
    return controlador.renderizar_documento_por_id(id)

@app.post('/documento/crear')
def crear_documento():
    texto = request.form.get('form-texto')
    return controlador.renderizar_documento_creado(texto)

@app.route('/guardar_evento')
def crear_evento():
    from aplicacion.modelo.evento_academico import EventoAcademico
    from aplicacion.modelo.tema_evento import TemaEvento
    from aplicacion.config import db

    evento = EventoAcademico(nombre='SI',
                            edicion= 16,
                            tematica= 'Pruebas de tesis', 
                            presentacion='Buscando mil formas de usar SQLAlchemy')
    tema1 = TemaEvento(tema='Prueba1')
    tema2 = TemaEvento(tema='Prueba2')
    tema3 = TemaEvento(tema='Prueba3')
    tema4 = TemaEvento(tema='Prueba4')

    evento.temas = [tema1, tema2, tema3, tema4]

    db.session.add(evento)
    db.session.commit()
    return ''

@app.route('/guardar_persona')
def crear_persona():
    from aplicacion.modelo.persona_academica import PersonaAcademica
    from aplicacion.modelo.automovil import Automovil
    from aplicacion.config import db

    ponente = PersonaAcademica(nombre='Edwar', correo='edwar2@gmail.com', contrasenia=hashlib.sha256('123'.encode()).hexdigest(), es_administrador=False)
    auto = Automovil(placa='1122D1', 
                      modelo='Honda',
                      anio='2018',
                      color='Negro',)

    ponente.automovil = auto

    db.session.add(ponente)
    db.session.commit()
    return ''