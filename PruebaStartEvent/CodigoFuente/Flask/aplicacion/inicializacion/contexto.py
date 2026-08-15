

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

def registrar_rutas(app):
    
    with app.app_context():       
        from aplicacion.blueprints.archivos import archivos_bp
        from aplicacion.blueprints.documento_evento import documento_evento_bp
        from aplicacion.blueprints.autenticacion import autenticacion_bp
        from aplicacion.blueprints.evento import evento_academico_bp
        
        app.register_blueprint(archivos_bp)
        app.register_blueprint(documento_evento_bp)
        app.register_blueprint(autenticacion_bp)
        app.register_blueprint(evento_academico_bp)
        