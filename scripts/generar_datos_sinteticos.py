"""Genera datos SINTÉTICOS (no reales) para el PMV, con defectos intencionales."""
import random
from pathlib import Path

import pandas as pd

SEMILLA = 42
N_ESTUDIANTES = 300
PERIODOS = ["2025-10", "2025-20", "2026-10"]
PROGRAMAS = ["Ingeniería de Sistemas", "Ingeniería Civil", "Administración",
             "Contabilidad", "Derecho"]

random.seed(SEMILLA)
salida = Path("data")
salida.mkdir(exist_ok=True)
ids = [f"E{n:05d}" for n in range(1, N_ESTUDIANTES + 1)]

# --- Académico ---
filas = []
for e in ids:
    programa = random.choice(PROGRAMAS)
    ciclo_base = random.randint(1, 8)
    for i, p in enumerate(PERIODOS):
        filas.append({
            "id_estudiante": e, "programa": programa,
            "ciclo": min(10, ciclo_base + i), "periodo": p,
            "promedio": round(min(20, max(5, random.gauss(13, 3))), 2),
            "cursos": random.randint(4, 7),
        })
acad = pd.DataFrame(filas)
acad.loc[acad.sample(frac=0.03, random_state=1).index, "promedio"] = None  # vacíos
acad.loc[acad.sample(n=5, random_state=2).index, "promedio"] = 25          # fuera de rango
acad = pd.concat([acad, acad.sample(n=10, random_state=3)], ignore_index=True)  # duplicados

# --- Socioeconómico ---
soc = pd.DataFrame({
    "id_estudiante": ids,
    "quintil_ingreso": [random.randint(1, 5) for _ in ids],
    "zona": random.choices(["Urbana", "Rural"], weights=[65, 35], k=len(ids)),
    "trabaja": random.choices(["Si", "No"], weights=[40, 60], k=len(ids)),
})
soc.loc[soc.sample(n=8, random_state=4).index, "quintil_ingreso"] = None

# --- LMS ---
lms = pd.DataFrame([
    {"id_estudiante": e, "periodo": p,
     "actividad": random.randint(0, 40), "frecuencia": random.randint(0, 7)}
    for e in ids for p in PERIODOS
])
lms.loc[lms.sample(n=10, random_state=5).index, "frecuencia"] = None

acad.to_csv(salida / "academico.csv", index=False, encoding="utf-8")
soc.to_csv(salida / "socioeconomico.csv", index=False, encoding="utf-8")
lms.to_csv(salida / "lms.csv", index=False, encoding="utf-8")
print(f"academico: {len(acad)} filas | socioeconomico: {len(soc)} | lms: {len(lms)}")