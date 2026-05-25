from src.validators import validar_cpf


def test_aceita_cpf_valido():
    assert validar_cpf("111.444.777-35") is True
