def is_url_long(url, threshold=70):
    """Verifica se a URL é considerada longa.
    
    Args:
        url (str): A URL a ser analisada.
        threshold (int): Limite de caracteres considerado longo.
        
    Returns:
        bool: True se a URL é longa, False caso contrário.
    """
    return len(url) >= threshold 