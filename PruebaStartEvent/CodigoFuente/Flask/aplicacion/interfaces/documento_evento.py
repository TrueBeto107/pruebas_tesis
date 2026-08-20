from abc import ABC
from abc import abstractmethod
from aplicacion.inicializacion.extenciones import db

class DocumentoEventoRepositorioI(ABC):
    
    @abstractmethod
    def select_by_edicion_y_subtipo():
        pass
