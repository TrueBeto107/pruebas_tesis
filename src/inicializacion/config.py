from datetime import timedelta
from pathlib import Path

ARCHIVO_EJECUTANDODSE = Path(__file__).resolve()  # config.py
DIRECTORIO_STARTEVENT = ARCHIVO_EJECUTANDODSE.parents[
    2
]  # 2 padres arriba de wsgi.py. "/StartEvent"


class Config:
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://admin_agent:9q70MdN915@localhost:5432/isolated_db_test"
    )
    JWT_SECRET_KEY = "123"
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_POR_EXPIRAR = timedelta(minutes=30)
    DIRECTORIO_DOCUMENTOS = DIRECTORIO_STARTEVENT / "Documentos"
    DIRECTORIO_BACKUP = DIRECTORIO_STARTEVENT / "Backups"
    DIRECTORIO_TEMPLATES = DIRECTORIO_STARTEVENT / "src" / "templates"
    # pepper = secrets.token_bytes(32).hex()
    PIMIENTA = "3098d9ada2f3ca6afc68a4f8e4accd9823008872aba7de5e50e347871d733ed8"


class DevelopmentConfig(Config):
    DEBUG = True
    JWT_COOKIE_SECURE = False


class ProductionConfig(Config):
    DEBUG = False
    JWT_COOKIE_SECURE = True
