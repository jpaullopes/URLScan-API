from tldextract import extract

# Lista de TLDs comumente usados em phishing
SUSPECTS_TLDS = [
    "zip", "mov", "xyz", "top", "info", "live", "gq", 
    "cf", "tk", "ml", "work", "link", "click"
]

# Função que verifica se o TLD é suspeito
def suspect_tld_verificator(url):   
    extracted_tlds = extract(url).suffix
    return extracted_tlds in SUSPECTS_TLDS