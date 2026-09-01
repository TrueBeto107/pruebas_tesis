from src.blueprints.archivos import crear_archivos_blueprint
from src.blueprints.autenticacion import crear_autenticacion_blueprint
from src.blueprints.documento_evento import crear_documento_blueprint
from src.blueprints.evento import crear_evento_blueprint
from src.blueprints.startevent import crear_startevent_blueprint
from src.controlador.archivos import ArchivosControlador
from src.controlador.autenticacion import AutenticacionControlador
from src.controlador.documento_evento import DocumentoControlador
from src.controlador.evento import EventosControlador
from src.controlador.startevent import StarteventControlador
from src.repositorio.comite_evento import ComiteEventoRepositorio
from src.repositorio.documento_evento import DocumentoEventoRepositorio
from src.repositorio.persona_academica import PersonaAcademicaRepositorio
from src.servicio.archivos import ArchivoServicio
from src.servicio.autenticacion import AutenticadorServicio
from src.servicio.documento_evento import DocumentoEventoServicio
from src.servicio.evento import EventosServicio
from src.servicio.startevent import StarteventServicio


def crear_base(app, db):
    with app.app_context():
        from src.modelo.actividad import Actividad
        from src.modelo.actividad_compartida import ActividadCompartida
        from src.modelo.agenda import Agenda
        from src.modelo.asistencia import Asistencia
        from src.modelo.automovil import Automovil
        from src.modelo.autoridad import Autoridad
        from src.modelo.clasificacion_persona import ClasificacionPersona
        from src.modelo.codigo_contrasenia import CodigoContrasenia
        from src.modelo.color_evento import ColorEvento
        from src.modelo.comite_evento import ComiteEvento
        from src.modelo.convocatoria_actividad import ConvocatoriaActividad
        from src.modelo.documento_evento import DocumentoEvento
        from src.modelo.espacio import Espacio
        from src.modelo.evento_academico import EventoAcademico
        from src.modelo.fecha_espacio import FechaEspacio
        from src.modelo.fecha_plantel import FechaPlantel
        from src.modelo.fecha_preferencial import FechaPreferencial
        from src.modelo.horario_actividad import HorarioActividad
        from src.modelo.palabra_clave_actividad import PalabraClaveActividad
        from src.modelo.participante import Participante
        from src.modelo.persona_academica import PersonaAcademica
        from src.modelo.plantel import Plantel
        from src.modelo.propiedades_actividad import PropiedadesActividad
        from src.modelo.requisicion import Requisicion
        from src.modelo.telefono_persona import TelefonoPersona
        from src.modelo.tema_evento import TemaEvento

        db.create_all()


def componer_de_raiz(app):

    documento_evento_repositorio = DocumentoEventoRepositorio()
    persona_academica_repositorio = PersonaAcademicaRepositorio()
    comite_evento_repositorio = ComiteEventoRepositorio()

    startevent_servicio = StarteventServicio()
    archivo_servicio = ArchivoServicio()
    autenticacion_servicio = AutenticadorServicio(persona_academica_repositorio)
    documento_evento_servicio = DocumentoEventoServicio(documento_evento_repositorio)
    eventos_servicio = EventosServicio(
        comite_evento_repositorio, documento_evento_repositorio
    )

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
