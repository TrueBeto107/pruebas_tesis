from flask import current_app as app
from flask import send_from_directory

class FlaskServicio:
    def otorgar_documento(self, filename):
        return send_from_directory(app.config['DIRECTORIO_DOCUMENTOS'], filename)