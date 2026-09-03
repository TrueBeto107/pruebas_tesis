"""Módulo de inicialización principal de la aplicación StartEvent.

Este módulo proporciona la función crear_app() que configura e inicializa
la aplicación Flask con todas las extensiones, base de datos, rutas y
componentes necesarios.
"""

from flask import Flask

from src.inicializacion.backup import registrar_backup
from src.inicializacion.config import DevelopmentConfig
from src.inicializacion.contexto import componer_de_raiz, crear_base
from src.inicializacion.extenciones import db, jwt


def crear_app():
    """Crea e inicializa la aplicación Flask.

    Configura la aplicación Flask con la configuración de desarrollo,
    inicializa las extensiones, crea las tablas de
    base de datos, registra los blueprints y el comando de backup.

    Returns:
        app (Flask): instancia de la aplicación Flask configurada y lista para usar.

    """
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    jwt.init_app(app)

    crear_base(app, db)
    componer_de_raiz(app)
    registrar_backup(app)

    return app
