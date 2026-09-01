import enum


class AccesoOrganizador(enum.Enum):
    ORGANIZACION_EVENTO = "Organizacion_Evento"
    ORGANIZACION_TORNEOS = "Organizacion_Torneos"
    GESTION_REQUISICIONES = "Gestion_Requisiciones"


class SubtipoDocumento(enum.Enum):
    # TipoDocumento.DOCUMENTO_EVENTO
    PLANEACION_REQUISICIONES = "Planeacion_Requisiciones"
    REPORTE_FINAL = "Reporte_Final"
    # TipoDocumento.DOCUMENTO_PROMOCIONAL
    LOGOTIPO = "Logotipo"
    BANNER_VERTICAL = "Banner"
    BANNER_HORIZONTAL = "Banner_Horizontal"
    CARTEL_PROMOCIONAL = "Cartel_Promocional"
    PALETA_COLORES = "Paleta_Colores"
    # TipoDocumento.DOCUMENTO_CONVOCATORIA
    CONVOCATORIA_ACADEMICA = "Convocatoria_Academica"
    CONVOCATORIA_ESTUDIANTIL = "Convocatoria_Estudiantil"
    # TipoDocumento.DOCUMENTO_PLANTEL
    ACUSE_ESPACIOS = "Acuse_Espacios"
    FONDO_CONSTANCIA = "Fondo_Constancia"
    LISTA_ESTACIONAMIENTO = "Lista_Estacionamiento"
    AGENDA_ACTIVIDADES = "Agenda_Actividades"
    AGENDA_ACTIVIDADES_CULTURALES = "Agenda_Actividades_Culturales"
    AGENDA_POR_DIA = "Agenda_Por_Dia"
    LISTA_TALLERES = "Lista_Talleres"
    LISTA_TORNEOS = "Lista_Torneos"
    # TipoDocumento.DOCUMENTO_ORGANIZADOR
    CARTA_DISPENSA = "Carta_Dispensa"
    CONSTANCIA_ORGANIZADOR = "Constancia_Organizador"
    # TipoDocumento.DOCUMENTO_PONENTE
    CARTA_PRESENTACION = "Carta_Presentacion"
    # TipoDocumento.DOCUMENTO_ACTIVIDAD
    CONSTANCIA_EXPOSITOR = "Constancia_Expositor"
    CONSTANCIA_ASISTENTE = "Constancia_Asistente"
    ACUSE_RECIBIDO = "Acuse_Recibido"
    NOTIFICACION_ACEPTACION = "Notificacion_Aceptacion"
    NOTIFICACION_RECHAZO = "Notificacion_Rechazo"
    NOTIFICACION_CALENDARIZACION = "Notificacion_Calendarizacion"
    CONFIRMACION_CALENDARIZACION = "Confirmacion_Calendarizacion"


class TipoDocumento(enum.Enum):
    DOCUMENTO_EVENTO = "Documento_Evento"
    DOCUMENTO_PROMOCIONAL = "Documento_Promocional"
    DOCUMENTO_CONVOCATORIA = "Documento_Convocatoria"
    DOCUMENTO_PLANTEL = "Documento_Plantel"
    DOCUMENTO_ORGANIZADOR = "Documento_Organizador"
    DOCUMENTO_PONENTE = "Documento_Ponente"
    DOCUMENTO_ACTIVIDAD = "Documento_Actividad"


class TipoAgenda(enum.Enum):
    PONENCIA = "Ponencia"
    TALLER = "Taller"
    COMPLEMENTARIA = "Complementaria"


class TipoColor(enum.Enum):
    TEXTO_TITULOS = "Texto_Titulos"
    TEXTO_SUBTITULOS = "Texto_Subtitulos"


class TipoTelefono(enum.Enum):
    EMPRESARIAL = "Empresarial"
    PERSONAL = "Personal"


class TipoPersona(enum.Enum):
    ORGANIZADOR = "Organizador"
    PARTICIPANTE = "Participante"


class SubtipoPersona(enum.Enum):
    PROFESOR = "Profesor"
    ESTUDIANTE = "Estudiante"
    COLABORADOR = "Colaborador"
    PONENTE = "Ponente"
    REPRESENTANTE = "Representante"
    ARTISTA = "Artista"
    TALLERISTA = "Tallerista"
    ASISTENTE = "Asistente"


class NivelEstudios(enum.Enum):
    LIC = "Lic."
    MTR = "Mtr."
    DR = "Dr."
    ING = "Ing."
    ESTUDIANTE = "Estudiante"


class EstadoActividad(enum.Enum):
    REVISION = "Revision"
    ACEPTADA = "Aceptada"
    RECHAZADA = "Rechazada"
    CANCELADA = "Cancelada"
    CONFIRMADA = "Confirmada"
    POR_VALIDAR = "Por_Validar"


class CarrerasUACM(enum.Enum):
    SOFTWARE = "Software"
    TRANSPORTE = "Transporte"
    MATEMATICAS = "Matematicas"
    ENERGIA = "Energia"
    ELECTRONICA = "Electronica"
    TELECOMUNICACIONES = "Telecomunicaciones"


# Se agrego enlace
class TipoAutoridad(enum.Enum):
    COORDINADOR_PLANTEL = "Coordinador_Plantel"
    COORDINADOR_COLEGIO = "Coodinador_Colegio"
    RECTOR = "Rector"
    ENLACE = "Enlace"


# Se cambio la enum
class TipoRequisicion(enum.Enum):
    LICITACION = "Licitacion"
    GASTOS_POR_COMPROBAR = "Gastos_Por_Comprobar"
    REEMBOLSO_DE_GASTOS = "Reembolso_De_Gastos"


# Se agrego generica
class TipoActividad(enum.Enum):
    PONENCIA = "Ponencia"
    PANEL = "Panel"
    TALLER = "Taller"
    PRESENTACION = "Presentacion"
    EXHIBICION = "Exhibicion"
    TORNEO = "Torneo"
    GENERICA = "Generica"


class TipoDocumentoEvento(enum.Enum):
    LOGOTIPO = "Logotipo"
    BANNER_VERTICAL = "Banner_Vertical"
    BANNER_HORIZONTAL = "Banner_Horizontal"
    CARTEL_PROMOCIONAL = "Cartel_Promocional"
    PALETA_DE_COLORES = "Paleta_De_Colores"
    CONVOCATORIA_PONENCIA_ACADEMICA = "Convocatoria_Ponencia_Academica"
    CONVOCATORIA_PONENCIA_ESTUDIANTIL = "Convocatoria_Ponencia_Estudiantil"
    PLANEACION_REQUISICIONES = "Planeacion_Requisiciones"
    ACUSE_DE_ESPACIOS = "Acuse_De_Espacios"


class TipoInstitucion(enum.Enum):
    SECTOR_PUBLICO = "Sector_Publico"
    SECTOR_PRIVADO = "Sector_Privado"
    SECTOR_ESTUDIANTIL = "Sector_Estudiantil"
    SECTOR_ACADEMICO = "Sector_Academico"


class TipoParticipante(enum.Enum):
    EXPOSITOR = "Expositor"
    RESPONSABLE = "Responsable"


class EstadoActivo(enum.Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    PENDIENTE = "Pendiente"
