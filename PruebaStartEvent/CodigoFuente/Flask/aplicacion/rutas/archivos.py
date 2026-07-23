from flask import current_app as app
from aplicacion.servicio.archivos import FlaskServicio
flask_servicio = FlaskServicio()

@app.route('/documento/<path:filename>')
def documentos(filename):
    return flask_servicio.otorgar_documento(filename)