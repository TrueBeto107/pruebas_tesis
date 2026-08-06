from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from sqlalchemy import text

db = SQLAlchemy()
jwt = JWTManager()

@jwt.user_identity_loader
def sustituir_usuario(usuario):
    return str(usuario.id_persona_academica)

@jwt.user_lookup_loader
def definir_current_user(_, jwt_data):
    identidad = int(jwt_data["sub"])
    user = db.session.execute(text('SELECT id_persona_academica, nombre FROM persona_academica WHERE id_persona_academica = :id'), {"id": identidad}).fetchone()
    return user