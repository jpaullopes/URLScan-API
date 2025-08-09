import src.shortener_checker as shortener_checker

# Exemplo de uso

# Caso 1: URL curta suspeita
url_curta_suspeita = "https://bit.ly/3xYz12"
resultado1 = shortener_checker.is_blacklisted(url_curta_suspeita)
print(f"Analisando '{url_curta_suspeita}': {resultado1}")  # Deve imprimir True
# Caso 2: URL normal
url_normal = "https://www.google.com"
resultado2 = shortener_checker.is_blacklisted(url_normal)
print(f"Analisando '{url_normal}': {resultado2}")  # Deve imprimir False