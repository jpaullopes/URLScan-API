import hashlib
import os

import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()
API_KEY = os.getenv("API_KEY_VIRUSTOTAL")

# Gera hash SHA-256 da URL.
def get_url_hash(url):
    return hashlib.sha256(url.encode()).hexdigest()

# Constrói a URL da API do VirusTotal.
def build_api_url(url_hash):
    if not API_KEY:
        print("Erro: Chave de API do VirusTotal não encontrada no arquivo .env")
        return None
    return f"https://www.virustotal.com/api/v3/urls/{url_hash}"

# Função para verificar a URL no VirusTotal
def check_url_virustotal(url):
    try:
        url_hash = get_url_hash(url)
        api_url = build_api_url(url_hash)
        
        if not api_url:
            return None
            
        headers = {
            "x-apikey": API_KEY
        }
        response = requests.get(api_url, headers=headers)
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

# Função para obter a quantidade de análises maliciosas
def get_virustotal_malicious_number(url):
    response = check_url_virustotal(url)
    if not response or 'data' not in response:
        return 0
    try:
        stats = response['data']['attributes']['last_analysis_stats']
        return stats.get('malicious', 0)
    except (KeyError, TypeError):
        return 0


