from tldextract import extract

# Lista de TLDs comumente usados em phishing
SUSPICIOUS_TLDS = [
    "zip", "mov", "xyz", "top", "info", "live", "gq", 
    "cf", "tk", "ml", "work", "link", "click"
]


def is_suspicious_tld(url):
    """Verifica se o TLD da URL é suspeito.
    
    Args:
        url (str): A URL a ser analisada.
        
    Returns:
        bool: True se o TLD é suspeito, False caso contrário.
    """
    extracted_tld = extract(url).suffix
    return extracted_tld in SUSPICIOUS_TLDS