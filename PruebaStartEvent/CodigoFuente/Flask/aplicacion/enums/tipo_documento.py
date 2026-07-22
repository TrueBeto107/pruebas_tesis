import enum

class TipoDocumento(enum.Enum):
    DOCUMENTO_EVENTO = 'Documento_Evento'
    DOCUMENTO_PROMOCIONAL = 'Documento_Promocional'
    DOCUMENTO_CONVOCATORIA = 'Documento_Convocatoria'
    DOCUMENTO_PLANTEL = 'Documento_Plantel'
    DOCUMENTO_ORGANIZADOR = 'Documento_Organizador'
    DOCUMENTO_PONENTE = 'Documento_Ponente'
    DOCUMENTO_ACTIVIDAD = 'Documento_Actividad'