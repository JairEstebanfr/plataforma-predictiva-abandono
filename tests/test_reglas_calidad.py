from src.domain.registro_academico import RegistroAcademico as R
from src.domain.reglas_calidad import validar_registros


def reg(id_="E1", periodo="2025-10", prom=14.0):
    return R(id_, "Sistemas", 3, periodo, prom, 5)


def test_tu01_detecta_campos_faltantes_y_rango():
    res = validar_registros([reg(prom=None), reg("E2", prom=25.0), reg("E3")])
    assert len(res.validos) == 1
    assert len(res.errores) == 2


def test_tu02_detecta_duplicados():
    res = validar_registros([reg(), reg()])
    assert len(res.validos) == 1
    assert any("duplicado" in e for e in res.errores)


def test_tu03_indice_calidad():
    res = validar_registros([reg(), reg("E2"), reg("E3", prom=None), reg("E4", prom=30)])
    assert res.indice_calidad == 50.0