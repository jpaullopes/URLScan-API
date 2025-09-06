import json
import os
from urllib.parse import urlparse
from tldextract import extract
from re import search
import requests
from bs4 import BeautifulSoup
import whois
from datetime import datetime

class PhishingAnalyzer:
    def __init__(self, config_path=None):
        if config_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(base_dir, '..', '..' , 'config.json')

        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.domain_cache = {}

    def analyze(self, url):
        points = 0
        rules_triggered = []
        ml_features = {}

        # --- Análise Heurística e Extração de Features ---

        # Regras baseadas na estrutura da URL
        if self._is_long(url):
            points += self.config["weights"]["is_long"]
            rules_triggered.append("url_longa")

        if self._is_suspicious_tld(url):
            points += self.config["weights"]["is_suspicious_tld"]
            rules_triggered.append("tld_suspeito")

        if self._has_excessive_subdomains(url):
            points += self.config["weights"]["has_excessive_subdomains"]
            rules_triggered.append("excesso_de_subdominios")

        if self._is_shortener(url):
            points += self.config["weights"]["is_shortener"]
            rules_triggered.append("encurtador_de_url")

        if self._has_obfuscation(url):
            points += self.config["weights"]["has_obfuscation"]
            rules_triggered.append("ofuscacao_com_@")

        if self._has_ip(url):
            points += self.config["weights"]["has_ip"]
            rules_triggered.append("uso_de_ip")
            ml_features['ip'] = 1
        else:
            ml_features['ip'] = 0

        # Extração de features para o modelo de ML
        extracted_url = extract(url)
        ml_features['nb_www'] = 1 if 'www' in extracted_url.subdomain else 0
        ml_features['ratio_digits_url'] = sum(c.isdigit() for c in url) / len(url) if len(url) > 0 else 0
        ml_features['nb_qm'] = url.count('?')
        
        suspicious_words = ['login', 'verify', 'account', 'security', 'update', 'confirm', 'banco', 'caixa']
        hints = sum(word in url.lower() for word in suspicious_words)
        ml_features['phish_hints'] = hints
        if hints > 0:
            points += 15 * hints
            rules_triggered.append("palavras_suspeitas")

        # Análise de conteúdo e WHOIS (agora retorna os pontos adicionais)
        points += self._analyze_content_and_whois(url, ml_features, rules_triggered)

        risk_level = self._get_risk_level(points)

        return {
            "heuristic_results": {
                "pontuacao_de_risco": points,
                "nivel_risco": risk_level,
                "regras_acionadas": list(set(rules_triggered))
            },
            "ml_features": ml_features
        }

    def _analyze_content_and_whois(self, url, ml_features, rules_triggered):
        points_to_add = 0
        try:
            extracted_url = extract(url)
            domain = f"{extracted_url.domain}.{extracted_url.suffix}"

            # WHOIS
            if domain in self.domain_cache:
                domain_age = self.domain_cache[domain]
            else:
                domain_info = whois.whois(domain)
                if domain_info and domain_info.creation_date:
                    creation_date = domain_info.creation_date[0] if isinstance(domain_info.creation_date, list) else domain_info.creation_date
                    domain_age = (datetime.now() - creation_date).days
                    self.domain_cache[domain] = domain_age
                else:
                    domain_age = -1
            ml_features['domain_age'] = domain_age
            if 0 <= domain_age < 180:
                points_to_add += 20
                rules_triggered.append("dominio_recente")

            # Análise de conteúdo da página
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
            response = requests.get(url, timeout=7, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            ml_features['nb_hyperlinks'] = len(soup.find_all('a'))
            
            title = soup.title.string if soup.title else ''
            if domain.lower() not in title.lower():
                ml_features['domain_in_title'] = 0
                points_to_add += 15
                rules_triggered.append("dominio_fora_do_titulo")
            else:
                ml_features['domain_in_title'] = 1

        except Exception as e:
            print(f"Erro ao acessar/analisar a URL {url}: {e}")
            ml_features['domain_age'] = -1
            ml_features['nb_hyperlinks'] = -1
            ml_features['domain_in_title'] = -1
            points_to_add += 10
            rules_triggered.append("pagina_nao_acessivel")
        
        return points_to_add

    def _is_long(self, url):
        return len(url) >= self.config["thresholds"]["long_url"]

    def _is_suspicious_tld(self, url):
        extracted_tld = extract(url).suffix
        return extracted_tld in self.config["tlds"]

    def _has_excessive_subdomains(self, url):
        hostname = urlparse(url).hostname
        if hostname is None:
            return False
        return hostname.count(".") >= self.config["thresholds"]["subdomain"]

    def _is_shortener(self, url):
        hostname = urlparse(url).hostname
        return hostname in self.config["shorteners"]

    def _has_obfuscation(self, url):
        return '@' in url

    def _has_ip(self, url):
        ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
        return search(ip_pattern, url) is not None
        
    def _get_risk_level(self, points):
        if points > 70:
            return "Nível 5: Risco Crítico"
        elif points > 50:
            return "Nível 4: Risco Alto"
        elif points > 25:
            return "Nível 3: Risco Médio"
        elif points > 0:
            return "Nível 2: Risco Baixo"
        else:
            return "Nível 0: Nenhuma Ameaça"
