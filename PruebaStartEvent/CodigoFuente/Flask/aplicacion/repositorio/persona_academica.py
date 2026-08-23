from aplicacion.modelo.persona_academica import PersonaAcademica
from aplicacion.interfaces.repositorio import PersonaAcademicaRepositorioI
from aplicacion.inicializacion.extenciones import db
from sqlalchemy import select

class PersonaAcademicaRepositorio(PersonaAcademicaRepositorioI):
    
    def select_by_correo(self, correo: str) -> PersonaAcademica | None:
        stmt = select(PersonaAcademica).where(PersonaAcademica.correo == correo)
        return db.session.scalars(stmt).one_or_none()