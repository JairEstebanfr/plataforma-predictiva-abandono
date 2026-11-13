from src.adapters.csv_academico import CsvAcademicoAdapter
from src.domain.reglas_calidad import validar_registros


def test_ti01_carga_y_valida_datos_academicos():
    registros = CsvAcademicoAdapter("data/academico.csv").leer()
    res = validar_registros(registros)
    print(f"procesados={res.procesados} validos={len(res.validos)} "
          f"errores={len(res.errores)} calidad={res.indice_calidad:.1f}%")
    assert res.procesados == 910
    assert len(res.errores) > 0  # los defectos sintéticos se detectan
    assert 0 < res.indice_calidad < 100