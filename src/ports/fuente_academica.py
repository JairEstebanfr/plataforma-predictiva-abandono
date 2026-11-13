from abc import ABC, abstractmethod
from typing import List

from src.domain.registro_academico import RegistroAcademico


class FuenteAcademicaPort(ABC):
    @abstractmethod
    def leer(self) -> List[RegistroAcademico]:
        """Devuelve los registros académicos de la fuente."""