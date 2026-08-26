from src.servicio.archivos import ArchivoServicio


class ArchivosControlador:
    def __init__(self, servicio: ArchivoServicio) -> None:
        self.servicio = servicio

    def otorgar_documento(self, filename):
        return self.servicio.otorgar_documento(filename)
