import argparse

# Função para configurar os argumentos da linha de comando
def configure_arguments():
    
    parser = argparse.ArgumentParser(
    description="Analisa URLs para phishing.",
    epilog="Exemplo de uso:\npython3 main.py --url 'http://example.com'\npython3 main.py --file arquivo.txt --speed",
    formatter_class=argparse.RawTextHelpFormatter
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="Analisa uma única URL.")
    group.add_argument("-f", "--file", dest="filename", help="Analisa uma lista de URLs de um arquivo de texto.")
    
    parser.add_argument("-s", "--speed", action="store_true", help="No modo de arquivo, executa a análise rápida sem usar a API do VirusTotal.")
    
    return parser.parse_args()

