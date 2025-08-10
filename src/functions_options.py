import obfuscation      # Verifica obfuscação na URL
import suspect_tld_verificator  # Verifica TLD suspeito
import url_counter      # Verifica comprimento da URL
import subdomain_counter    # Conta subdomínios
import shortener_checker    # Verifica se é encurtador
import ip_formatation_indetification  # Verifica se há IP
import virus_total_verificator  # Verifica no VirusTotal
import time # Importa a biblioteca time para pausas

# Função que calcula os pontos de uma URL com base em várias verificações
def calculator_url_points(url):
    points = 0

    if url_counter.is_url_long(url):  # URL longa
        points += 10
    if suspect_tld_verificator.is_suspicious_tld(url):  # TLD suspeito
        points += 15
    if subdomain_counter.has_excessive_subdomains(url):  # Muitos subdomínios
        points += 15
    if shortener_checker.is_url_shortener(url):   # Encurtador conhecido
        points += 15
    if obfuscation.obfuscation_verification(url):  # Obfuscação
        points += 20
    if ip_formatation_indetification.ip_verification(url):  # IP na URL
        points += 35

    return points

# Classifica o nível de risco
def verify_url(url):

    virus_malicious_count = virus_total_verificator.get_virustotal_malicious_number(url)

    if virus_malicious_count is not None and virus_malicious_count > 0:
        return "Nível 5: Risco Crítico \n Descrição: A URL foi identificada como maliciosa pelo VirusTotal. Evite o acesso."

    return verify_url_speed(url)

def verify_url_speed(url):
    
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
    
def speed_verificator(file):
    try:
        with open(file,'r') as fi:
            for line in fi:
                url = line.strip()
                result = verify_url_speed(url)
                print(f"URL: {url}\nResultado: {result}\n")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file}' não encontrado.")



def file_verificator(file):
    counter = 0
    try:
        with open(file,'r') as fi:
            for line in fi:
                url = line.strip()
                result = verify_url(url)
                print(f"URL: {url}\nResultado: {result}\n")
                time.sleep(15)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file}' não encontrado.")