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
    for domain in BLACK_LIST:
        if domain in url:
            return True
    return False