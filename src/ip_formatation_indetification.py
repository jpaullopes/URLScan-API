from re import search

# Função para verificar se uma URL contém um endereço IP
def ip_verification(url):
    padron =  r"(\d{1,3}\.){3}\d{1,3}"
    return search(padron,url) is not None