from urllib.parse import urlparse


def extract_hostname(url):
    """Extrai o hostname da URL.
    
    Args:
        url (str): A URL a ser analisada.
        
    Returns:
        str: O hostname da URL ou None se inválida.
    """
    return urlparse(url).hostname


def count_subdomains(url):
    """Conta a quantidade de subdomínios na URL.
    
    Args:
        url (str): A URL a ser analisada.
        
    Returns:
        int: Número de subdomínios (pontos no hostname).
    """
    hostname = extract_hostname(url)
    if hostname is None:
        return 0
    return hostname.count(".")


def has_excessive_subdomains(url, threshold=3):
    """Verifica se a URL tem muitos subdomínios.
    
    Args:
        url (str): A URL a ser analisada.
        threshold (int): Limite de subdomínios considerado excessivo.
        
    Returns:
        bool: True se tem muitos subdomínios, False caso contrário.
    """
    return count_subdomains(url) >= threshold