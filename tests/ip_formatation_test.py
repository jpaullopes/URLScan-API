import src.ip_formatation_indetification as ip_formatation

# Exemplo de uso

# Caso 1: URL com endereço IP
url_com_ip = "http://192.168.0.1/login"
resultado1 = ip_formatation.ip_verification(url_com_ip)
print(f"Analisando '{url_com_ip}': {resultado1}") 

# Caso 2: URL sem endereço IP
url_sem_ip = "https://www.google.com"
resultado2 = ip_formatation.ip_verification(url_sem_ip)
print(f"Analisando '{url_sem_ip}': {resultado2}") 