from aplicacion.modelo.persona_academica import PersonaAcademica
from aplicacion.config import db

class PersonaAcademicaRepositorio:
    def select(self, persona_academica: PersonaAcademica) -> PersonaAcademica:
        # Usar filter_by con condiciones múltiples
        usuario = db.session.query(PersonaAcademica).filter_by(correo=persona_academica.correo).first()        
        return usuario