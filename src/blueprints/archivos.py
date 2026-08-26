from flask import Blueprint
from flask import current_app as app

from src.controlador.archivos import ArchivosControlador


def crear_archivos_blueprint(controlador: ArchivosControlador):
    archivos_bp = Blueprint(
        "archivo",
        __name__,
        url_prefix="/archivo",
        template_folder=app.config["DIRECTORIO_TEMPLATES"] / "archivo",
    )

    @archivos_bp.route("/documento/<path:filename>")
    def documentos(filename):
        return controlador.otorgar_documento(filename)

    return archivos_bp
