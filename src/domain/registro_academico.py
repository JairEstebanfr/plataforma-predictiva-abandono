from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class RegistroAcademico:
    id_estudiante: str
    programa: str
    ciclo: int
    periodo: str
    promedio: Optional[float]
    cursos: int