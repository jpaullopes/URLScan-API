import pytest
from src.core.obfuscation import obfuscation_verification

def test_benchmark_obfuscation_verification(benchmark):
    """
    Testa a performance da função obfuscation_verification.
    """
    result = benchmark(obfuscation_verification, "http://example.com")
    assert result is False

def test_benchmark_obfuscation_verification_with_at(benchmark):
    """
    Testa a performance da função obfuscation_verification com um '@' na URL.
    """
    result = benchmark(obfuscation_verification, "http://user@example.com")
    assert result is True
