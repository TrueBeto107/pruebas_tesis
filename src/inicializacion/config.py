"""Módulo de configuración de la aplicación StartEvent.

Define las clases de configuración para desarrollo, producción y testing
"""

from datetime import timedelta
from pathlib import Path

ARCHIVO_EJECUTANDODSE = Path(__file__).resolve()  # config.py
DIRECTORIO_STARTEVENT = ARCHIVO_EJECUTANDODSE.parents[
    2
]  # 2 padres arriba de wsgi.py. "/StartEvent"


class Config:
    """Clase base de configuración con variables comunes.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): URI de conexión a PostgreSQL.
        JWT_SECRET_KEY (str): clave secreta para firmar tokens JWT.
        JWT_TOKEN_LOCATION (list): ubicaciones donde se buscan los tokens.
        JWT_ACCESS_TOKEN_EXPIRES (timedelta): tiempo de expiración del token de acceso.
        JWT_REFRESH_TOKEN_EXPIRES (timedelta): tiempo de expiración del token de
        refrescar.
        JWT_POR_EXPIRAR (timedelta): tiempo antes de que el token se considere próximo
        a expirar.
        DIRECTORIO_DOCUMENTOS (Path): ruta al directorio de documentos.
        DIRECTORIO_BACKUP (Path): ruta al directorio de backups.
        DIRECTORIO_TEMPLATES (Path): ruta al directorio de templates HTML.
        PIMIENTA (str): clave de encriptación adicional para hash de contraseñas.

    """

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://admin_agent:9q70MdN915@localhost:5432/isolated_db_test"
    JWT_SECRET_KEY = "123"
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_POR_EXPIRAR = timedelta(minutes=30)
    DIRECTORIO_DOCUMENTOS = DIRECTORIO_STARTEVENT / "Documentos"
    DIRECTORIO_BACKUP = DIRECTORIO_STARTEVENT / "Backups"
    DIRECTORIO_TEMPLATES = DIRECTORIO_STARTEVENT / "src" / "templates"
    # pepper = secrets.token_bytes(32).hex()
    PIMIENTA = (
        "3098d9ada2f3ca6afc68a4f8e4accd9823008872aba7de5e50e347871d733ed8"
    )


class DevelopmentConfig(Config):
    """Clase de configuración para el desarrollo local.

    Attributes:
        DEBUG (bool): activa el modo debug de Flask.
        JWT_COOKIE_SECURE (bool): desactiva las cookies seguras por HTTP

    """

    DEBUG = True
    JWT_COOKIE_SECURE = False


class ProductionConfig(Config):
    """Clase de configuraciíon para el entorno de producción.

    Attributes:
        DEBUG (bool): desactiva el modo debug de Flask.
        JWT_COOKIE_SECURE (bool): activa las cookies seguras por HTTP

    """

    DEBUG = False
    JWT_COOKIE_SECURE = True
