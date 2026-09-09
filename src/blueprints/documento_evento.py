"""Blueprint definitions for document and event management routes."""

import hashlib
import secrets

from flask import Blueprint, Response, render_template, request
from flask import current_app as app
from flask_jwt_extended import jwt_required

from src.controlador.documento_evento import DocumentoControlador
from src.enums import AccesoOrganizador, EstadoActivo
from src.modelo.comite_evento import ComiteEvento
from src.modelo.plantel import Plantel


def crear_documento_blueprint(controlador: DocumentoControlador) -> Blueprint:
    """Create the document blueprint and register its routes.

    Args:
        controlador: Controller responsible for document CRUD and rendering.

    Returns:
        Blueprint: Flask blueprint configured with the document endpoints.

    """
    documento_evento_bp = Blueprint(
        "documento",
        __name__,
        url_prefix="/documento",
        template_folder=app.config["DIRECTORIO_TEMPLATES"] / "documento",
    )

    @app.route("/prueba_v")
    def mostrar_vista_vertical() -> str:
        """Render the vertical version of the main page.

        Args:
            None.

        Returns:
            str: HTML content for the vertical page template.

        """
        return render_template("pagina_inicio.html")

    @app.route("/prueba_cv")
    def mostrar_vista_vc() -> str:
        """Render the column-based layout preview page.

        Args:
            None.

        Returns:
            str: HTML content for the columns template.

        """
        return render_template("pagina_columnas.html")

    @app.route("/registro_ponente")
    def mostrar_registro_ponente() -> str:
        """Render the speaker registration form.

        Args:
            None.

        Returns:
            str: HTML content for the registration template.

        """
        return render_template("form_registro_PA.html")

    @documento_evento_bp.route("/")
    @jwt_required()
    def gestion_documentos() -> Response | str:
        """Show the document management page for the current user.

        Args:
            None.

        Returns:
            Response | str: The rendered document management page.

        """
        return controlador.rederizar_gestion_documentos()

    @documento_evento_bp.route("/tabla")
    def actualizar_tabla() -> Response | str:
        """Refresh the document table content.

        Args:
            None.

        Returns:
            Response | str: The updated table view payload.

        """
        return controlador.renderizar_tabla()

    @documento_evento_bp.route("/mostrar/<ruta>")
    def mostrar(ruta: str) -> Response | str:
        """Render a document identified by its route path.

        Args:
            ruta: Unique path or identifier of the document to show.

        Returns:
            Response | str: The rendered document response.

        """
        return controlador.renderizar_documento(ruta)

    @documento_evento_bp.get("/buscar")
    def get_documento() -> Response | str:
        """Fetch a document by its identifier from the request query.

        Args:
            None.

        Returns:
            Response | str: The document content or rendered response.

        """
        return controlador.renderizar_documento_por_id()

    @documento_evento_bp.post("/crear")
    def crear_documento() -> Response | str:
        """Create a new document from submitted text.

        Args:
            None.

        Returns:
            Response | str: The created document response.

        """
        texto: str | None = request.form.get("form-texto")
        return controlador.renderizar_documento_creado(texto)

    @app.route("/crear_admin")
    def crear_evento() -> str:
        """Create a sample event and store it in the database.

        Args:
            None.

        Returns:
            str: Empty string after the sample event is persisted.

        """
        from src.enums import SubtipoDocumento, TipoDocumento
        from src.inicializacion.extenciones import db
        from src.modelo.automovil import Automovil
        from src.modelo.documento_evento import DocumentoEvento
        from src.modelo.evento_academico import EventoAcademico
        from src.modelo.persona_academica import PersonaAcademica
        from src.modelo.tema_evento import TemaEvento

        sal = secrets.token_bytes()
        admin = PersonaAcademica(
                    nombres="Admin",
                    apellido_paterno="Test",
                    correo_contacto="a@g",
                    contrasenia=hashlib.sha256(
                        b"123" + sal + bytes.fromhex(app.config["PIMIENTA"])
                    ).hexdigest(),
                    es_administrador=True,
                    estado_activo=EstadoActivo.ACTIVO,
                    sal=sal.hex(),
                )
        db.session.add(admin)
        db.session.commit()
        return ""

    @app.route('/test')
    def playground():
        return render_template('test.html')

    return documento_evento_bp
