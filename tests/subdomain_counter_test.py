from src.subdomain_counter import subdomain_alert

url_normal = "https://www.google.com"
url_suspeita = "https://login.conta.bancaria.seguranca.xyz.com/entrar"

print(f"Analisando '{url_normal}': {subdomain_alert(url_normal)}")
print(f"Analisando '{url_suspeita}': {subdomain_alert(url_suspeita)}")