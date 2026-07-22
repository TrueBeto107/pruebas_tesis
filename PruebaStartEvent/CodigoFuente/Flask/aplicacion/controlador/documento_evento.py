from flask import current_app as app
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from aplicacion.servicio.documento_evento import DocumentoEventoServicio
from aplicacion.dto.documento_evento import CrearDocumentoDto
from aplicacion.dto.documento_evento import BuscarDocumentoDto
documento_evento_servicio = DocumentoEventoServicio()

@app.route('/documento')
def gestion_documentos():
    lista_documentos = documento_evento_servicio.buscar_documentos()
    return render_template('buscar_documento.html', documentos=lista_documentos)

@app.route('/tabla')
def actualizar_tabla():
    lista_documentos = documento_evento_servicio.buscar_documentos()
    return render_template('tabla.html', documentos =lista_documentos)

@app.route('/mostrar/<ruta>')
def mostrar(ruta):
    return render_template('visor.html', ruta_archivo=ruta)

@app.get('/documento/buscar')
def get_documento():
    id = request.args.get('id_documento')
    dto = BuscarDocumentoDto()
    dto.id_documento_evento = id
    dto_respuesta = documento_evento_servicio.buscar_documento(dto)
    return render_template('visor.html', ruta_archivo=dto_respuesta.ruta_archivo)

@app.post('/documento/crear')
def crear_documento():
    texto = request.form.get('form-texto')
    dto = CrearDocumentoDto()
    dto.texto = texto
    dto_salida = documento_evento_servicio.crear_documento(dto)
    return render_template('visor.html', ruta_archivo=dto_salida.ruta_archivo)

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

    ponente = PersonaAcademica(nombre='Pepe')
    auto = Automovil(placa='1122D1', 
                      modelo='Honda',
                      anio='2018',
                      color='Negro')

    ponente.automovil = auto

    db.session.add(ponente)
    db.session.commit()
    return ''