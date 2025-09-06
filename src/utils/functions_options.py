import time
from src.core.analyzer import PhishingAnalyzer
from src.utils import virustotal

def format_analysis_result(analysis):
    risk_level = analysis['risk_level']
    points = analysis['points']
    
    descriptions = {
        "Nível 0: Nenhuma Ameaça": "A URL passou limpa em todas as verificações.",
        "Nível 1: Risco Mínimo": "Detectado um único sinal de baixo impacto. Provavelmente seguro, mas incomum.",
        "Nível 2: Risco Baixo": "Detectado um sinal moderado ou múltiplos sinais de baixo impacto. Requer atenção.",
        "Nível 3: Risco Médio": "Detectado um sinal forte ou uma combinação significativa de outros sinais. A URL é suspeita.",
        "Nível 4: Risco Alto": "Combina um sinal forte com outros indicadores, ou possui múltiplos sinais moderados. Alta probabilidade de ser maliciosa.",
        "Nível 5: Risco Crítico": "Múltiplos sinais de alerta graves foram acionados. Evite o acesso. Praticamente certo de ser phishing."
    }
    
    description = descriptions.get(risk_level, "Descrição não disponível.")
    
    return f"{risk_level} ({points} pontos)\nDescrição: {description}"


def verify_url(url):
    analyzer = PhishingAnalyzer()
    
    virus_malicious_count = virustotal.get_virustotal_malicious_number(url)

    if virus_malicious_count is not None and virus_malicious_count > 0:
        return "Nível 5: Risco Crítico \n Descrição: A URL foi identificada como maliciosa pelo VirusTotal. Evite o acesso."

    analysis = analyzer.analyze(url)
    return format_analysis_result(analysis)


def verify_url_speed(url):
    analyzer = PhishingAnalyzer()
    analysis = analyzer.analyze(url)
    return format_analysis_result(analysis)


def speed_verificator(file):
    try:
        with open(file, 'r') as fi:
            for line in fi:
                url = line.strip()
                if url:
                    result = verify_url_speed(url)
                    print(f"URL: {url}\nResultado: {result}\n")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file}' não encontrado.")


def normal_verificator(file):
    try:
        with open(file, 'r') as fi:
            for line in fi:
                url = line.strip()
                if url:
                    result = verify_url(url)
                    print(f"URL: {url}\nResultado: {result}\n")
                    time.sleep(15)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file}' não encontrado.")