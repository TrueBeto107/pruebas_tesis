from flask import Flask
from aplicacion.inicializacion.extenciones import db
from aplicacion.inicializacion.extenciones import jwt
from aplicacion.inicializacion.config import DevelopmentConfig
from aplicacion.inicializacion.contexto import crear_base
from aplicacion.inicializacion.contexto import registrar_rutas
from aplicacion.inicializacion.backup import registrar_backup

def crear_app():
    app = Flask(__name__)
    
    app.config.from_object(DevelopmentConfig)
    
    db.init_app(app)
    jwt.init_app(app)
    
    crear_base(app, db)
    registrar_rutas(app)
    registrar_backup(app)
    
    return app
