import obfuscation
import suspect_tld_verificator
import url_counter
import subdomain_counter
import shortener_checker
import ip_formatation_indetification

# Função que calcula os pontos de uma URL com base em várias verificações
def calculator_url_points(url):
    points = 0

    if url_counter.url_counter(url):
        points += 10
    if suspect_tld_verificator.suspect_tld_verificator(url):
        points += 15
    if subdomain_counter.subdomain_alert(url):
        points += 15
    if shortener_checker.shortener_checker(url):    
        points += 15
    if obfuscation.obfuscation_function_verificator(url):
        points += 20
    if ip_formatation_indetification.ip_verification(url):
        points += 35

    return points

def verify_url(url):
    points = calculator_url_points(url)
    
    if points == 0:
        return "Nível 0: Nenhuma Ameaça (0 pontos)\nDescrição: A URL passou limpa em todas as verificações."
    elif 1 <= points <= 15:
        return "Nível 1: Risco Mínimo (1-15 pontos)\nDescrição: Detectado um único sinal de baixo impacto. Provavelmente seguro, mas incomum."
    elif 16 <= points <= 30:
        return "Nível 2: Risco Baixo (16-30 pontos)\nDescrição: Detectado um sinal moderado ou múltiplos sinais de baixo impacto. Requer atenção."
    elif 31 <= points <= 50:
        return "Nível 3: Risco Médio (31-50 pontos)\nDescrição: Detectado um sinal forte ou uma combinação significativa de outros sinais. A URL é suspeita."
    elif 51 <= points <= 70:
        return "Nível 4: Risco Alto (51-70 pontos)\nDescrição: Combina um sinal forte com outros indicadores, ou possui múltiplos sinais moderados. Alta probabilidade de ser maliciosa."
    else:  
        return "Nível 5: Risco Crítico (Acima de 70 pontos)\nDescrição: Múltiplos sinais de alerta graves foram acionados. Evite o acesso. Praticamente certo de ser phishing."

def main():
    url = input("Digite a URL para análise: ")
    resultado = verify_url(url)
    print(resultado)

if __name__ == "__main__":
    main()