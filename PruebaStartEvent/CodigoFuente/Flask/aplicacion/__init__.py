from flask import Flask
from aplicacion.inicializacion.extenciones import db
from flask_jwt_extended import JWTManager
from aplicacion.inicializacion.config import DevelopmentConfig, ARCHIVO_EJECUTANDODSE, DIRECTORIO_STARTEVENT
from aplicacion.inicializacion.contexto import crear_base
from aplicacion.inicializacion.contexto import registrar_rutas
from aplicacion.inicializacion.backup import registrar_backup

def crear_app():
    app = Flask(__name__)
    
    app.config.from_object(DevelopmentConfig)
    
    db.init_app(app)
    jwt = JWTManager(app)
    
    crear_base(app, db)
    registrar_rutas(app)
    registrar_backup(app)
    
    return app
