import json
import os
from urllib.parse import urlparse
from tldextract import extract
from re import search

class PhishingAnalyzer:
    def __init__(self, config_path=None):
        if config_path is None:
            # Build a path to the config file relative to this file
            base_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(base_dir, '..', 'config.json')

        with open(config_path, 'r') as f:
            self.config = json.load(f)

    def analyze(self, url):
        results = {
            "url": url,
            "points": 0,
            "rules_triggered": []
        }

        # Rule checks
        if self._is_long(url):
            results["points"] += self.config["weights"]["is_long"]
            results["rules_triggered"].append("is_long")

        if self._is_suspicious_tld(url):
            results["points"] += self.config["weights"]["is_suspicious_tld"]
            results["rules_triggered"].append("is_suspicious_tld")

        if self._has_excessive_subdomains(url):
            results["points"] += self.config["weights"]["has_excessive_subdomains"]
            results["rules_triggered"].append("has_excessive_subdomains")

        if self._is_shortener(url):
            results["points"] += self.config["weights"]["is_shortener"]
            results["rules_triggered"].append("is_shortener")

        if self._has_obfuscation(url):
            results["points"] += self.config["weights"]["has_obfuscation"]
            results["rules_triggered"].append("has_obfuscation")

        if self._has_ip(url):
            results["points"] += self.config["weights"]["has_ip"]
            results["rules_triggered"].append("has_ip")
            
        results["risk_level"] = self._get_risk_level(results["points"])

        return results

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
        if points == 0:
            return "Nível 0: Nenhuma Ameaça"
        elif 1 <= points <= 15:
            return "Nível 1: Risco Mínimo"
        elif 16 <= points <= 30:
            return "Nível 2: Risco Baixo"
        elif 31 <= points <= 50:
            return "Nível 3: Risco Médio"
        elif 51 <= points <= 70:
            return "Nível 4: Risco Alto"
        else:
            return "Nível 5: Risco Crítico"