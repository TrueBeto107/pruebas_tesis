from flask import current_app as app
from aplicacion.servicio.archivos import ArchivoServicio
from flask import Blueprint

archivos_bp = Blueprint(
    'archivo',
    __name__,
    url_prefix='/archivo',
    template_folder=app.config['DIRECTORIO_TEMPLATES'] / 'archivo'
    )
archivo_servicio = ArchivoServicio()

@archivos_bp.route('/documento/<path:filename>')
def documentos(filename):
    return archivo_servicio.otorgar_documento(filename)

