from src.core.ip_detection import ip_verification

def test_ip_verification():
    # Caso 1: URL com endereço IP
    url_com_ip = "http://192.168.0.1/login"
    assert ip_verification(url_com_ip) is True

    # Caso 2: URL sem endereço IP
    url_sem_ip = "https://www.google.com"
    assert ip_verification(url_sem_ip) is False
