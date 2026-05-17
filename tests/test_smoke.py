"""Smoke tests: verify the package imports and basic functions work."""

from __future__ import annotations


def test_import_gerador_module() -> None:
    """The gerador module must be importable."""
    import gerador

    assert gerador is not None


def test_import_gerador_class() -> None:
    """The GeradorEgera class must be importable from gerador."""
    from gerador import GeradorEgera

    assert GeradorEgera is not None


def test_gerador_instantiation() -> None:
    """GeradorEgera must instantiate without errors."""
    from gerador import GeradorEgera

    gerador = GeradorEgera()
    assert gerador is not None


def test_gerar_palavra_returns_non_empty_string() -> None:
    """gerar_palavra must return a non-empty string."""
    from gerador import GeradorEgera

    palavra = GeradorEgera().gerar_palavra()
    assert isinstance(palavra, str)
    assert len(palavra) > 0


def test_known_input_output_adicionar_acento() -> None:
    """adicionar_acento must produce known accented output for a known input."""
    from gerador import GeradorEgera

    gerador = GeradorEgera()
    assert gerador.adicionar_acento("ca") == "cá"
    assert gerador.adicionar_acento("pro") == "pró"
    assert gerador.adicionar_acento("fi") == "fí"


def test_known_input_already_accented_unchanged() -> None:
    """adicionar_acento must be idempotent on already-accented syllables."""
    from gerador import GeradorEgera

    gerador = GeradorEgera()
    for silaba in ["pró", "fí", "sô", "bál"]:
        assert gerador.adicionar_acento(silaba) == silaba


def test_calcular_maximo_is_positive_integer() -> None:
    """calcular_maximo_palavras must return a positive int."""
    from gerador import GeradorEgera

    maximo = GeradorEgera().calcular_maximo_palavras()
    assert isinstance(maximo, int)
    assert maximo > 0
