from urllib.parse import urlparse

BLACK_LIST = [
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

# Função para verificar se uma URL está na lista negra
def is_blacklisted(url):
    hostname_url = urlparse(url).hostname
    return hostname_url in BLACK_LIST