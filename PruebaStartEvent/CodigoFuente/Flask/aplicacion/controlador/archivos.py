from flask import current_app as app
from aplicacion.servicio.archivos import ArchivoServicio
flask_servicio = ArchivoServicio()

@app.route('/documento/<path:filename>')
def documentos(filename):
    return flask_servicio.otorgar_documento(filename)