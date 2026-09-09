"""Definición del blueprint para peticiones sobre StartEvent.

Note:
    El blueprint se define dentro de una función para inyectar las dependencias
    del controlador.

"""

import hashlib
import secrets
import subprocess
from pathlib import Path

from flask import Blueprint, Response
from flask import current_app as app
from sqlalchemy import text

from src.controlador.startevent import StarteventControlador
from src.enums import EstadoActivo
from src.inicializacion.base_datos import crear_base
from src.inicializacion.extenciones import db


def crear_startevent_blueprint(
    controlador: StarteventControlador,
) -> Blueprint:
    """Crea y configura el blueprint de StartEvent.

    Mapea todos los endpoints hacia el controlador y comandos de flask

    Args:
        controlador (StarteventControlador): Instancia del controlador para
        atender las peticiones.

    Returns:
        Blueprint: el blueprint configurado con todos los endpoints

    """
    startevent_bp = Blueprint(
        "startevent",
        __name__,
        url_prefix="/startevent",
        template_folder=app.config["DIRECTORIO_TEMPLATES"] / "startevent",
    )

    @startevent_bp.route("/")
    def login() -> str:
        """Muestra la página de Login para StartEvent.

        Returns:
            str: El HTML de la página de Login.

        """
        return controlador.renderizar_login()

    @startevent_bp.after_request
    def refresh(response: Response) -> Response:
        """Refresca las cookies de acceso de JWT si estan por expirar.

        Este método se ejecuta tras todos los endpoint del blueprint de
        StartEvent

        Args:
            response (Response): El objeto Response que iba a ser enviado al
            cliente.

        Returns:
            Response: La respuesta con las cookies refrescadas si es el caso,
            la misma respuesta sin modificar si no.

        """
        return controlador.refrescar_tokens_por_expirar(response)

    @startevent_bp.cli.command("format")
    def autoformatear() -> None:
        """Formatea automáticamente el código de todo el proyecto.

        Indica los errores según la configuración de pyproject.toml, corrige
        los que sea posible y muestra el resto de los errores.

        Note:
            Equivalente a ejecutar
            ruff format
            ruff check --fix
            djlint . --reformat
            djlint . --lint

        Examples:
            flask startevent format

        """
        print(  # noqa: T201
            "---------------------------------------------\n"
            "\tFormateando archivos python...\n"
            "---------------------------------------------\n"
        )
        subprocess.run(["ruff", "format"])
        print(  # noqa: T201
            "---------------------------------------------\n"
            "\tAnalizando archivos python...\n"
            "---------------------------------------------\n"
        )
        subprocess.run(["ruff", "check", "--fix"])
        print(  # noqa: T201
            "---------------------------------------------\n"
            "\tFormateando archivos HTML...\n"
            "---------------------------------------------\n"
        )
        subprocess.run(["djlint", ".", "--reformat"])
        print(  # noqa: T201
            "---------------------------------------------\n"
            "\tAnalizando archivos HTML...\n"
            "---------------------------------------------\n"
        )
        subprocess.run(["djlint", ".", "--lint"])
        print(  # noqa: T201
            "-------------------------------------\n"
            "\tProyecto formateado.\n"
            "-------------------------------------\n"
            "Corregir todos los errores encontrados.\n"
        )

    @startevent_bp.cli.command("crear_base_prueba")
    def crear_base_prueba() -> None:
        crear_base(app, db)
        archivo = Path.open(
            app.config["DIRECTORIO_BACKUP"] / "backup_prueba.sql"
        )
        sql = archivo.read()
        db.session.execute(text(sql))
        db.session.commit()

    return startevent_bp
