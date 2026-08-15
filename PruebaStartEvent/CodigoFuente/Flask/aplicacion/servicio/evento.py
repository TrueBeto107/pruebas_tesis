from aplicacion.modelo.documento_evento import DocumentoEvento
from aplicacion.repositorio.eventos import EventosRepositorio
from aplicacion.dto.evento import MostrarEventoDto
from aplicacion.repositorio.comite_evento import ComiteEventoRepositorio
from aplicacion.repositorio.documento_evento import DocumentoEventoRepositorio
from aplicacion.enums.tipo_documento import TipoDocumento
from aplicacion.enums.subtipo_documento import SubtipoDocumento
from aplicacion.modelo.documento_evento import DocumentoEvento
from aplicacion.dto.evento import BuscarEventosUsuarioDto


class EventosServicio:
    
    repositorio = EventosRepositorio()
    repositorio_comite_evento = ComiteEventoRepositorio()
    repositorio_documento_evento = DocumentoEventoRepositorio()
    
    def buscar_eventos(self, dto: BuscarEventosUsuarioDto):
        lista_comites = self.repositorio_comite_evento.select_by_persona_id(dto.id_usuario)
        dtos = []
        for comite in lista_comites:
            documento = DocumentoEvento(
                id_evento=comite.id_evento_academico, 
                tipo_documento=TipoDocumento.DOCUMENTO_PROMOCIONAL, 
                subtipo_documento=SubtipoDocumento.LOGOTIPO)
            documento_evento = self.repositorio_documento_evento.select_by_edicion_y_subtipo(documento)
            dto = MostrarEventoDto(
                nombre=comite.evento_academico.nombre,
                edicion=comite.evento_academico.edicion,
                ruta_logotipo=documento_evento[0].ruta_archivo
            )
            
            dtos.append(dto)
        return dtos