from flask import Flask
from src.inicializacion.extenciones import db
from src.inicializacion.extenciones import jwt
from src.inicializacion.config import DevelopmentConfig
from src.inicializacion.contexto import crear_base
from src.inicializacion.contexto import componer_de_raiz
from src.inicializacion.backup import registrar_backup

def crear_app():
    app = Flask(__name__)
    
    app.config.from_object(DevelopmentConfig)
    
    db.init_app(app)
    jwt.init_app(app)
    
    crear_base(app, db)
    componer_de_raiz(app)
    registrar_backup(app)
    
    return app


