import os
import hashlib
from dotenv import load_dotenv
import requests


# Carrega as variáveis de ambiente
load_dotenv()
API_KEY = os.getenv("API_KEY_VIRUSTOTAL")


def _get_url_hash(url):
    """Gera hash SHA-256 da URL.
    
    Args:
        url (str): A URL para gerar o hash.
        
    Returns:
        str: Hash SHA-256 da URL.
    """
    return hashlib.sha256(url.encode()).hexdigest()


def _build_api_url(url_hash):
    """Constrói a URL da API do VirusTotal.
    
    Args:
        url_hash (str): Hash SHA-256 da URL.
        
    Returns:
        str: URL completa da API ou None se sem chave.
    """
    if not API_KEY:
        print("Erro: Chave de API do VirusTotal não encontrada no arquivo .env")
        return None
    return f"https://www.virustotal.com/api/v3/urls/{url_hash}"


def check_url_virustotal(url):
    """Verifica uma URL no VirusTotal.
    
    Args:
        url (str): A URL a ser verificada.
        
    Returns:
        dict: Resposta JSON da API do VirusTotal ou None se erro.
    """
    try:
        url_hash = _get_url_hash(url)
        api_url = _build_api_url(url_hash)
        
        if not api_url:
            return None
            
        headers = {"x-apikey": API_KEY}
        response = requests.get(api_url, headers=headers)
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None
    


