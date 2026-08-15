from pathlib import Path
from datetime import timedelta

ARCHIVO_EJECUTANDODSE = Path(__file__).resolve()                    #config.py
DIRECTORIO_STARTEVENT = ARCHIVO_EJECUTANDODSE.parents[4]  #4 padres arriba de wsgi.py. "/StartEvent"

class Config:                                                   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin_agent:9q70MdN915@localhost:5432/isolated_db_test'
    JWT_SECRET_KEY = '123'
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_POR_EXPIRAR = timedelta(minutes=30)
    DIRECTORIO_DOCUMENTOS = DIRECTORIO_STARTEVENT / 'Documentos'
    DIRECTORIO_BASE_FLASK = ARCHIVO_EJECUTANDODSE.parents[2]  # "/Flask"
    DIRECTORIO_BACKUP = DIRECTORIO_STARTEVENT / 'Backups'
    DIRECTORIO_TEMPLATES = DIRECTORIO_BASE_FLASK / 'aplicacion' / 'templates'

class DevelopmentConfig(Config):
    DEBUG = True
    JWT_COOKIE_SECURE = False

class ProductionConfig(Config):
    DEBUG = False
    JWT_COOKIE_SECURE = True  