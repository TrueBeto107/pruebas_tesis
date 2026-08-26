from flask import Blueprint
from flask import current_app as app

from src.controlador.startevent import StarteventControlador


def crear_startevent_blueprint(controlador: StarteventControlador):
    startevent_bp = Blueprint(
        "startevent",
        __name__,
        url_prefix="/startevent",
        template_folder=app.config["DIRECTORIO_TEMPLATES"] / "startevent",
    )

    @startevent_bp.route("/")
    def login():
        return controlador.renderizar_login()

    @startevent_bp.after_request
    def refresh(response):
        return controlador.refrescar_tokens_por_expirar(response)

    return startevent_bp
