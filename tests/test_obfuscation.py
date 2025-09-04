from src.core.obfuscation import obfuscation_verification

def test_obfuscation_verification():
    # Caso 1: URL suspeita
    url_maliciosa = "http://pagamento-seguro.com@site-estranho.net/login"
    assert obfuscation_verification(url_maliciosa) is True

    # Caso 2: URL normal
    url_legitima = "https://www.google.com"
    assert obfuscation_verification(url_legitima) is False
