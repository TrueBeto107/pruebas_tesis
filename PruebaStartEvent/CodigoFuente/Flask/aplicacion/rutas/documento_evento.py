from flask import current_app as app
from flask import request
from aplicacion.servicio.documento_evento import DocumentoEventoServicio
from aplicacion.modelo.comite_evento import ComiteEvento
from aplicacion.servicio.evento import EventosServicio  
from aplicacion.controlador.documento_evento import DocumentoControlador
from aplicacion.controlador.evento import EventosControlador
from aplicacion.enums.tipo_documento import TipoDocumento
from aplicacion.enums.subtipo_documento import SubtipoDocumento
from aplicacion.enums.acceso_organizador import AccesoOrganizador
from aplicacion.modelo.plantel import Plantel

from flask import render_template
from flask_jwt_extended import jwt_required
import hashlib

controlador = DocumentoControlador(DocumentoEventoServicio())
eventos_controlador = EventosControlador(EventosServicio())




@app.route('/documento')
@jwt_required()
def gestion_documentos():
    return controlador.rederizar_gestion_documentos()

@app.route('/tabla')
def actualizar_tabla():
    return controlador.renderizar_tabla()

@app.route('/mostrar/<ruta>')
def mostrar(ruta):
    return controlador.renderizar_documento(ruta)

@app.get('/documento/buscar')
def get_documento():
    return controlador.renderizar_documento_por_id()

@app.post('/documento/crear')
def crear_documento():
    texto = request.form.get('form-texto')
    return controlador.renderizar_documento_creado(texto)

@app.route('/guardar_evento')
def crear_evento():
    from aplicacion.modelo.evento_academico import EventoAcademico
    from aplicacion.modelo.tema_evento import TemaEvento
    from aplicacion.modelo.documento_evento import DocumentoEvento
    from aplicacion.enums.tipo_documento import TipoDocumento
    from aplicacion.enums.subtipo_documento import SubtipoDocumento
    from aplicacion.inicializacion.extenciones import db
    from aplicacion.modelo.persona_academica import PersonaAcademica
    from aplicacion.modelo.automovil import Automovil
    
    evento = EventoAcademico(nombre='Simposio de ingenieria ',
                            edicion= 11,
                            tematica= 'Pruebas de tesis', 
                            presentacion='Buscando mil formas de usar SQLAlchemy')
    tema1 = TemaEvento(tema='Prueba1')
    tema2 = TemaEvento(tema='Prueba2')
    tema3 = TemaEvento(tema='Prueba3')
    tema4 = TemaEvento(tema='Prueba4')
    
    ponente = PersonaAcademica(nombre='Edwar', correo='e@gmail.com', contrasenia=hashlib.sha256('123'.encode()).hexdigest(), es_administrador=False)
    auto = Automovil(placa='1122D1', 
                      modelo='Honda',
                      anio='2018',
                      color='Negro',)
    ponente.automovil = auto
    
    logo = DocumentoEvento(tipo_documento=TipoDocumento.DOCUMENTO_PROMOCIONAL, subtipo_documento=SubtipoDocumento.LOGOTIPO, ruta_archivo='Logo_11.png')

    evento.temas = [tema1, tema2, tema3, tema4]
    evento.documentos = [logo]
    
    plantel = Plantel(abreviatura='SLT', nombre='San Lorenzo Tezonco', correo_contacto='', direccion='')
    comite = ComiteEvento(acceso_organizador=AccesoOrganizador.ORGANIZACION_EVENTO)
    
    comite.persona = ponente
    comite.plantel = plantel
    evento.comite_evento = comite
    
    db.session.add(evento)
    db.session.commit()
    return ''