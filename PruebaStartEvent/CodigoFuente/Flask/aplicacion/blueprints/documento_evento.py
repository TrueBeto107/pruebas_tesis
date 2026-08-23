from flask import current_app as app
from flask import request
from flask import Blueprint
from aplicacion.servicio.documento_evento import DocumentoEventoServicio
from aplicacion.modelo.comite_evento import ComiteEvento
from aplicacion.controlador.documento_evento import DocumentoControlador
from aplicacion.enums import AccesoOrganizador
from aplicacion.modelo.plantel import Plantel
from flask_jwt_extended import jwt_required
import hashlib
import secrets
from flask import render_template

def crear_documento_blueprint(controlador: DocumentoControlador):

    documento_evento_bp = Blueprint(
        'documento',
        __name__,
        url_prefix='/documento',
        template_folder=app.config['DIRECTORIO_TEMPLATES'] / 'documento'
        )

    @app.route('/prueba_v')
    def mostrar_vista_vertical():
        return render_template('pagina_inicio.html')

    @app.route('/prueba_cv')
    def mostrar_vista_vc():
        return render_template('pagina_columnas.html')

    @app.route('/registro_ponente')
    def mostrar_registro_ponente():
        return render_template('form_registro_PA.html')

    @documento_evento_bp.route('/')
    @jwt_required()
    def gestion_documentos():
        return controlador.rederizar_gestion_documentos()

    @documento_evento_bp.route('/tabla')
    def actualizar_tabla():
        return controlador.renderizar_tabla()

    @documento_evento_bp.route('/mostrar/<ruta>')
    def mostrar(ruta):
        return controlador.renderizar_documento(ruta)

    @documento_evento_bp.get('/buscar')
    def get_documento():
        return controlador.renderizar_documento_por_id()

    @documento_evento_bp.post('/crear')
    def crear_documento():
        texto = request.form.get('form-texto')
        return controlador.renderizar_documento_creado(texto)

    @app.route('/guardar_evento')
    def crear_evento():
        from aplicacion.modelo.evento_academico import EventoAcademico
        from aplicacion.modelo.tema_evento import TemaEvento
        from aplicacion.modelo.documento_evento import DocumentoEvento
        from aplicacion.enums import TipoDocumento
        from aplicacion.enums import SubtipoDocumento
        from aplicacion.inicializacion.extenciones import db
        from aplicacion.modelo.persona_academica import PersonaAcademica
        from aplicacion.modelo.automovil import Automovil
        
        evento = EventoAcademico(nombre='Simposio de ingenieria ',
                                edicion= 11,
                                tematica= 'Pruebas de tesis', 
                                presentacion='Buscando mil formas de usar SQLAlchemy')
        tema1 = TemaEvento(tema='Prueba1')
        tema2 = TemaEvento(tema='Prueba2')
        tema3 = TemaEvento(tema='Prueba3')
        tema4 = TemaEvento(tema='Prueba4')
        sal = secrets.token_bytes()
        ponente = PersonaAcademica(
            nombre='Edwar',
            correo='e@gmail.com',
            contrasenia=hashlib.sha256(
                '123'.encode() + 
                sal + 
                bytes.fromhex(app.config['PIMIENTA'])
                ).hexdigest(), 
            es_administrador=False, 
            sal=sal.hex())
        auto = Automovil(placa='1122D1', 
                        modelo='Honda',
                        anio='2018',
                        color='Negro',)
        ponente.automovil = auto
        
        logo = DocumentoEvento(tipo_documento=TipoDocumento.DOCUMENTO_PROMOCIONAL, subtipo_documento=SubtipoDocumento.LOGOTIPO, ruta_archivo='Logo_11.png')

        evento.temas = [tema1, tema2, tema3, tema4]
        evento.documentos = [logo]
        
        plantel = Plantel(abreviatura='SLT', nombre='San Lorenzo Tezonco', correo_contacto='', direccion='')
        comite = ComiteEvento(acceso_organizador=AccesoOrganizador.ORGANIZACION_EVENTO)
        
        comite.persona = ponente
        comite.plantel = plantel
        evento.comite_evento = comite
        
        db.session.add(evento)
        db.session.commit()
        return ''
    
    return documento_evento_bp