from urllib.parse import urlparse

# Função que separa o hostname da URL
def hostname_encounter(url):
    return urlparse(url).hostname

# Função que conta a quantidade de subdominos dentro do hostname
def subdomain_counter(url):
    hostname = hostname_encounter(url)
    return hostname.count(".")

# Função que retorna se os subdominos passaram ou são 3
def subdomain_alert(url):
    return subdomain_counter >= 3