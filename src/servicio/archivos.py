"""Proporciona acceso a archivos locales del sistema de archivos."""

from flask import current_app as app
from flask import send_from_directory


class ArchivoServicio:
    """Implementación del servicio para la entrega de archivos locales."""

    def otorgar_documento(self, filename):
        """Envía un documento guardado en el directorio configurado de Documentos."""
        return send_from_directory(
            app.config["DIRECTORIO_DOCUMENTOS"], filename
        )
