from aplicacion.modelo.documento_evento import DocumentoEvento
from aplicacion.dto.evento import MostrarEventoDto
from aplicacion.interfaces.repositorio import ComiteEventoRepositorioI
from aplicacion.interfaces.repositorio import DocumentoEventoRepositorioI
from aplicacion.enums.tipo_documento import TipoDocumento
from aplicacion.enums.subtipo_documento import SubtipoDocumento
from aplicacion.modelo.documento_evento import DocumentoEvento
from aplicacion.dto.evento import BuscarEventosUsuarioDto


class EventosServicio:
    
    def __init__(
        self, 
        repositorio_comite_evento: ComiteEventoRepositorioI, 
        repositorio_documento_evento: DocumentoEventoRepositorioI
        ) -> None:
        self.repositorio_comite_evento = repositorio_comite_evento
        self.repositorio_documento_evento = repositorio_documento_evento
    
    def buscar_eventos(self, dto: BuscarEventosUsuarioDto):
        lista_comites = self.repositorio_comite_evento.select_by_id_persona(dto.id_usuario)
        dtos = []
        for comite in lista_comites:
            documento_evento = self.repositorio_documento_evento.select_by_edicion_y_subtipo(
                comite.id_evento_academico,
                TipoDocumento.DOCUMENTO_PROMOCIONAL,
                SubtipoDocumento.LOGOTIPO
                )
            #N+1 evento academico
            dto_salida = MostrarEventoDto(
                nombre=comite.evento_academico.nombre,
                edicion=comite.evento_academico.edicion,
                ruta_logotipo=documento_evento[0].ruta_archivo
            )
            dtos.append(dto_salida)
        return dtos