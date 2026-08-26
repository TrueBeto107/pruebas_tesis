from sqlalchemy import select

from src.inicializacion.extenciones import db
from src.interfaces.repositorio import PersonaAcademicaRepositorioI
from src.modelo.persona_academica import PersonaAcademica


class PersonaAcademicaRepositorio(PersonaAcademicaRepositorioI):
    def select_by_correo(self, correo: str) -> PersonaAcademica | None:
        stmt = select(PersonaAcademica).where(PersonaAcademica.correo == correo)
        return db.session.scalars(stmt).one_or_none()
