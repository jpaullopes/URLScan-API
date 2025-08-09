from tldextract import extract

# Lista de TLDs comumente usados em phishing
SUSPECTS_TLD = [
    "zip", "mov", "xyz", "top", "info", "live", "gq", 
    "cf", "tk", "ml", "work", "link", "click"
]

# Função que verifica se o TLD é suspeito
def suspect_tld_verificator(url):   
    extracted_tld = extract(url).suffix
    return extracted_tld in SUSPECTS_TLD