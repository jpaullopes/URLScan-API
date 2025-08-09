from src.obfuscation import obfuscation_function

# Exemplo de uso

# Caso 1: URL suspeita
url_maliciosa = "http://pagamento-seguro.com@site-estranho.net/login"
resultado1 = obfuscation_function(url_maliciosa)
print(f"Analisando '{url_maliciosa}': {resultado1}") # Vai imprimir True

# Caso 2: URL normal
url_legitima = "https://www.google.com"
resultado2 = obfuscation_function(url_legitima)
print(f"Analisando '{url_legitima}': {resultado2}") # Vai imprimir False