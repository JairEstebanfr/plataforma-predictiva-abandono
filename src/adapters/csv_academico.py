from typing import List

import pandas as pd

from src.domain.registro_academico import RegistroAcademico
from src.ports.fuente_academica import FuenteAcademicaPort


class CsvAcademicoAdapter(FuenteAcademicaPort):
    def __init__(self, ruta: str):
        self.ruta = ruta

    def leer(self) -> List[RegistroAcademico]:
        df = pd.read_csv(self.ruta)
        df = df.astype(object).where(df.notna(), None)
        return [
            RegistroAcademico(
                id_estudiante=str(f["id_estudiante"]),
                programa=f["programa"],
                ciclo=int(f["ciclo"]),
                periodo=f["periodo"],
                promedio=None if f["promedio"] is None else float(f["promedio"]),
                cursos=int(f["cursos"]),
            )
            for f in df.to_dict("records")
        ]