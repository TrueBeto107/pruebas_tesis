def crear_base(app, db):
    with app.app_context():
        from aplicacion.modelo.evento_academico import EventoAcademico
        from aplicacion.modelo.tema_evento import TemaEvento
        from aplicacion.modelo.persona_academica import PersonaAcademica
        from aplicacion.modelo.automovil import Automovil
        from aplicacion.modelo.plantel import Plantel
        from aplicacion.modelo.actividad import Actividad
        from aplicacion.modelo.documento_evento import DocumentoEvento
        db.create_all()

def registrar_rutas(app):
    with app.app_context():
        from aplicacion.rutas import archivos
        from aplicacion.rutas import documento_evento
        from aplicacion.rutas import autenticacion