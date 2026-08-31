from flask import redirect, url_for
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()
jwt = JWTManager()


@jwt.user_identity_loader
def sustituir_usuario(usuario):
    return str(usuario.id_persona_academica)


@jwt.user_lookup_loader
def definir_current_user(_, jwt_data):
    identidad = int(jwt_data["sub"])
    return db.session.execute(
        text(
            "SELECT id_persona_academica, nombre, es_administrador FROM "
            "persona_academica WHERE id_persona_academica = :id"
        ),
        {"id": identidad},
    ).fetchone()


@jwt.expired_token_loader
def redireccionar_login(_, __):
    return redirect(url_for("login"))
