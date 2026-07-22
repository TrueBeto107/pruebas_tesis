from flask import Flask
from aplicacion.config import db
from pathlib import Path

from aplicacion.modelo.evento_academico import EventoAcademico

def crear_app():
    
    ARCHIVO_EJECUTANDODSE = Path(__file__).resolve()                    #wsgi.py
    DIRECTORIO_STARTEVENT = ARCHIVO_EJECUTANDODSE.parents[3]  #4 padres arriba de wsgi.py. "/StartEvent"
    DIRECTORIO_DOCUMENTOS = DIRECTORIO_STARTEVENT / 'Documentos'

    DIRECTORIO_BASE_FLASK = ARCHIVO_EJECUTANDODSE.parents[2]  # "/Flask"
    
    app = Flask(__name__)
                                                                   #usuario :  contraseña              /nombre_bd
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin_agent:9q70MdN915@localhost/isolated_db_test'
    app.config['DEBUG'] = True

    app.config['DIRECTORIO_DOCUMENTOS'] = DIRECTORIO_DOCUMENTOS
    app.config['DIRECTORIO_BASE_FLASK'] = DIRECTORIO_BASE_FLASK
    
    db.init_app(app)

    with app.app_context():
        from aplicacion.controlador import archivos
        from aplicacion.controlador import documento_evento
        
        from aplicacion.modelo.evento_academico import EventoAcademico
        from aplicacion.modelo.tema_evento import TemaEvento
        from aplicacion.modelo.persona_academica import PersonaAcademica
        from aplicacion.modelo.automovil import Automovil
        from aplicacion.modelo.plantel import Plantel
        from aplicacion.modelo.actividad import Actividad
        from aplicacion.modelo.documento_evento import DocumentoEvento
        
        db.create_all()
        return app