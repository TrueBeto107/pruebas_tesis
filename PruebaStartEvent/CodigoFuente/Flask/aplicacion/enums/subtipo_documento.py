import enum

class SubtipoDocumento(enum.Enum):
    #TipoDocumento.DOCUMENTO_EVENTO
    PLANEACION_REQUISICIONES = 'Planeacion_Requisiciones'
    REPORTE_FINAL = 'Reporte_Final'
    #TipoDocumento.DOCUMENTO_PROMOCIONAL
    LOGOTIPO = 'Logotipo'
    BANNER_VERTICAL = 'Banner'
    BANNER_HORIZONTAL = 'Banner_Horizontal'
    CARTEL_PROMOCIONAL = 'Cartel_Promocional'
    PALETA_COLORES = 'Paleta_Colores'
    #TipoDocumento.DOCUMENTO_CONVOCATORIA
    CONVOCATORIA_ACADEMICA = 'Convocatoria_Academica'
    CONVOCATORIA_ESTUDIANTIL = 'Convocatoria_Estudiantil'
    #TipoDocumento.DOCUMENTO_PLANTEL
    ACUSE_ESPACIOS = 'Acuse_Espacios'
    FONDO_CONSTANCIA = 'Fondo_Constancia'
    LISTA_ESTACIONAMIENTO = 'Lista_Estacionamiento'
    AGENDA_ACTIVIDADES = 'Agenda_Actividades'
    AGENDA_ACTIVIDADES_CULTURALES = 'Agenda_Actividades_Culturales'
    AGENDA_POR_DIA = 'Agenda_Por_Dia'
    LISTA_TALLERES = 'Lista_Talleres'
    LISTA_TORNEOS = 'Lista_Torneos'
    #TipoDocumento.DOCUMENTO_ORGANIZADOR
    CARTA_DISPENSA = 'Carta_Dispensa'
    CONSTANCIA_ORGANIZADOR = 'Constancia_Organizador'
    #TipoDocumento.DOCUMENTO_PONENTE
    CARTA_PRESENTACION = 'Carta_Presentacion'
    #TipoDocumento.DOCUMENTO_ACTIVIDAD
    CONSTANCIA_EXPOSITOR = 'Constancia_Expositor'
    CONSTANCIA_ASISTENTE = 'Constancia_Asistente'
    ACUSE_RECIBIDO = 'Acuse_Recibido'
    NOTIFICACION_ACEPTACION = 'Notificacion_Aceptacion'
    NOTIFICACION_RECHAZO = 'Notificacion_Rechazo'
    NOTIFICACION_CALENDARIZACION = 'Notificacion_Calendarizacion'
    CONFIRMACION_CALENDARIZACION = 'Confirmacion_Calendarizacion'