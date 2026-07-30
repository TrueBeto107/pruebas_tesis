from flask import Flask
from aplicacion.config import db
from pathlib import Path
from flask_jwt_extended import JWTManager
from aplicacion.modelo.evento_academico import EventoAcademico

def crear_app():
    
    ARCHIVO_EJECUTANDODSE = Path(__file__).resolve()                    #wsgi.py
    DIRECTORIO_STARTEVENT = ARCHIVO_EJECUTANDODSE.parents[3]  #4 padres arriba de wsgi.py. "/StartEvent"
    DIRECTORIO_DOCUMENTOS = DIRECTORIO_STARTEVENT / 'Documentos'

    DIRECTORIO_BASE_FLASK = ARCHIVO_EJECUTANDODSE.parents[2]  # "/Flask"
    
    app = Flask(__name__)
                                                                   #usuario :  contraseña           :puerto/nombre_bd
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin_agent:9q70MdN915@localhost:5432/isolated_db_test'
    
    app.config['DEBUG'] = True
    app.config['JWT_SECRET_KEY'] = '123'
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]

    app.config['DIRECTORIO_DOCUMENTOS'] = DIRECTORIO_DOCUMENTOS
    app.config['DIRECTORIO_BASE_FLASK'] = DIRECTORIO_BASE_FLASK
    
    db.init_app(app)
    jwt = JWTManager(app)

    with app.app_context():
        from aplicacion.rutas import archivos
        from aplicacion.rutas import documento_evento
        from aplicacion.rutas import autenticador
        
        from aplicacion.modelo.evento_academico import EventoAcademico
        from aplicacion.modelo.tema_evento import TemaEvento
        from aplicacion.modelo.persona_academica import PersonaAcademica
        from aplicacion.modelo.automovil import Automovil
        from aplicacion.modelo.plantel import Plantel
        from aplicacion.modelo.actividad import Actividad
        from aplicacion.modelo.documento_evento import DocumentoEvento
        
        db.create_all()
    # Comando para backup
    from aplicacion.backup import hacer_backup
    @app.cli.command('backup') 
    def backup_command():
        hacer_backup()

        
    return app
