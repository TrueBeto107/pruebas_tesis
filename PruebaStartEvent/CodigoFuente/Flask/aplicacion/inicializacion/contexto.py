from aplicacion.controlador.startevent import StarteventControlador
from aplicacion.servicio.startevent import StarteventServicio
from aplicacion.controlador.archivos import ArchivosControlador
from aplicacion.servicio.archivos import ArchivoServicio
from aplicacion.controlador.autenticacion import AutenticacionControlador
from aplicacion.servicio.autenticacion import AutenticadorServicio
from aplicacion.repositorio.persona_academica import PersonaAcademicaRepositorio
from aplicacion.controlador.documento_evento import DocumentoControlador
from aplicacion.servicio.documento_evento import DocumentoEventoServicio
from aplicacion.repositorio.documento_evento import DocumentoEventoRepositorio
from aplicacion.controlador.evento import EventosControlador
from aplicacion.servicio.evento import EventosServicio
from aplicacion.repositorio.comite_evento import ComiteEventoRepositorio
from aplicacion.blueprints.startevent import crear_startevent_blueprint
from aplicacion.blueprints.archivos import crear_archivos_blueprint
from aplicacion.blueprints.autenticacion import crear_autenticacion_blueprint
from aplicacion.blueprints.documento_evento import crear_documento_blueprint
from aplicacion.blueprints.evento import crear_evento_blueprint

def crear_base(app, db):
    with app.app_context():
        from aplicacion.modelo.evento_academico import EventoAcademico
        from aplicacion.modelo.tema_evento import TemaEvento
        from aplicacion.modelo.persona_academica import PersonaAcademica
        from aplicacion.modelo.automovil import Automovil
        from aplicacion.modelo.plantel import Plantel
        from aplicacion.modelo.actividad import Actividad
        from aplicacion.modelo.documento_evento import DocumentoEvento
        from aplicacion.modelo.comite_evento import ComiteEvento
        db.create_all()

def componer_de_raiz(app):
    
    documento_evento_repositorio = DocumentoEventoRepositorio()
    persona_academica_repositorio = PersonaAcademicaRepositorio()
    comite_evento_repositorio = ComiteEventoRepositorio()
    
    startevent_servicio = StarteventServicio()
    archivo_servicio = ArchivoServicio()
    autenticacion_servicio = AutenticadorServicio(persona_academica_repositorio)
    documento_evento_servicio = DocumentoEventoServicio(documento_evento_repositorio)
    eventos_servicio = EventosServicio(comite_evento_repositorio, documento_evento_repositorio)
    
    startevent_controlador = StarteventControlador(startevent_servicio)
    archivos_controlador = ArchivosControlador(archivo_servicio)
    autenticacion_controlador = AutenticacionControlador(autenticacion_servicio)
    documento_evento_controlador = DocumentoControlador(documento_evento_servicio)
    evento_academico_controlador = EventosControlador(eventos_servicio)
    
    with app.app_context():       
        startevent_bp = crear_startevent_blueprint(startevent_controlador)
        archivos_bp = crear_archivos_blueprint(archivos_controlador)
        autenticacion_bp = crear_autenticacion_blueprint(autenticacion_controlador)
        documento_evento_bp = crear_documento_blueprint(documento_evento_controlador)
        evento_academico_bp = crear_evento_blueprint(evento_academico_controlador)
        
        startevent_bp.register_blueprint(autenticacion_bp)
        startevent_bp.register_blueprint(evento_academico_bp)
        app.register_blueprint(startevent_bp)
        app.register_blueprint(archivos_bp)
        app.register_blueprint(documento_evento_bp)
        
        