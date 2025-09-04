from src.core.shortener_checker import is_url_shortener

def test_is_url_shortener():
    # Caso 1: URL curta suspeita
    url_curta_suspeita = "https://bit.ly/3xYz12"
    assert is_url_shortener(url_curta_suspeita) is True

    # Caso 2: URL normal
    url_normal = "https://www.google.com"
    assert is_url_shortener(url_normal) is False
