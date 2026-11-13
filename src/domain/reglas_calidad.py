from dataclasses import dataclass, field
from typing import List

from src.domain.registro_academico import RegistroAcademico


@dataclass
class ResultadoValidacion:
    procesados: int = 0
    validos: list = field(default_factory=list)
    errores: List[str] = field(default_factory=list)

    @property
    def indice_calidad(self) -> float:
        return 100 * len(self.validos) / self.procesados if self.procesados else 0.0


def validar_registros(registros: List[RegistroAcademico]) -> ResultadoValidacion:
    """TU-01: campos obligatorios y rango. TU-02: duplicados por (id_estudiante, periodo)."""
    res = ResultadoValidacion(procesados=len(registros))
    vistos = set()
    for r in registros:
        clave = (r.id_estudiante, r.periodo)
        if clave in vistos:
            res.errores.append(f"{clave}: duplicado")
            continue
        vistos.add(clave)
        if r.promedio is None:
            res.errores.append(f"{clave}: promedio vacio")
        elif not 0 <= r.promedio <= 20:
            res.errores.append(f"{clave}: promedio fuera de rango ({r.promedio})")
        else:
            res.validos.append(r)
    return res