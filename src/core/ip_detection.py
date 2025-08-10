from re import search


def ip_verification(url):
    """Verifica se uma URL contém um endereço IP.
    
    Args:
        url (str): A URL a ser analisada.
        
    Returns:
        bool: True se contém IP, False caso contrário.
    """
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    return search(ip_pattern, url) is not None