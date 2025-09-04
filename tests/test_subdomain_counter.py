from src.core.subdomain_counter import has_excessive_subdomains

def test_has_excessive_subdomains():
    url_normal = "https://www.google.com"
    url_suspeita = "https://login.conta.bancaria.seguranca.xyz.com/entrar"

    assert has_excessive_subdomains(url_normal) is False
    assert has_excessive_subdomains(url_suspeita) is True
