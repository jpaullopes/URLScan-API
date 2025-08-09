def obfuscation_verification(url):
    """Verifica se a URL contém caracteres de obfuscação suspeitos.
    
    Args:
        url (str): A URL a ser analisada.
        
    Returns:
        bool: True se contém obfuscação e False caso contrário.
    """
    return '@' in url


