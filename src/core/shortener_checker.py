from urllib.parse import urlparse


# Lista de serviços de encurtamento de URL conhecidos
URL_SHORTENERS = [
    "bit.ly",
    "t.co",         
    "tinyurl.com",
    "is.gd",
    "soo.gd",
    "ow.ly",
    "buff.ly",
    "rebrand.ly",
    "shorturl.at"
]


def is_url_shortener(url):
    """Verifica se uma URL é de um serviço de encurtamento conhecido.
    
    Args:
        url (str): A URL a ser analisada.
        
    Returns:
        bool: True se é um encurtador conhecido, False caso contrário.
    """
    hostname = urlparse(url).hostname
    return hostname in URL_SHORTENERS