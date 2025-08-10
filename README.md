# 🕵️ Phishing Analyzer Tool
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows-lightgrey)
![CLI](https://img.shields.io/badge/CLI-available-orange)

Analisador de URLs para detecção de características de phishing, desenvolvido como um projeto de portfólio para demonstrar habilidades em análise de segurança e desenvolvimento em Python.

## 📝 Descrição

Este projeto é uma ferramenta de linha de comando que avalia uma URL fornecida pelo usuário e calcula uma pontuação de risco com base em uma série de verificações heurísticas e na consulta a APIs de inteligência de ameaças. O objetivo é automatizar a análise inicial de links suspeitos, fornecendo um veredito rápido sobre o potencial de risco.

## ✨ Funcionalidades

O analisador utiliza uma abordagem multifacetada para avaliar as URLs, verificando os seguintes pontos:

### Análise Heurística (Interna)

 - **Uso de Endereço IP:** Detecta se a URL usa um endereço IP em vez de um nome de domínio.
 - **Caractere de Ofuscação (`@`):** Verifica a presença do caractere `@` na URL, uma técnica clássica de ofuscação.
 - **Excesso de Subdomínios:** Alerta para URLs com um número excessivo de subdomínios, usado para confundir o usuário.
 - **TLD Suspeito:** Compara o Top-Level Domain (ex: `.zip`, `.mov`) com uma lista de TLDs comumente abusados.
 - **Link Encurtado:** Identifica se a URL pertence a um serviço de encurtamento de links conhecido (ex: `bit.ly`).
 - **Comprimento Excessivo:** Sinaliza URLs anormalmente longas.

### Inteligência Externa

 - **Integração com VirusTotal:** Utiliza a API do VirusTotal para checar reputação contra mais de 70 serviços de segurança. Detecções críticas elevam o risco imediatamente.

## 🚀 Tecnologias Utilizadas

 - **Linguagem:** Python 3.8+
 - **Bibliotecas Principais:**
   - `requests`: Requisições HTTP
   - `python-dotenv`: Auxilia na leitura de variáveis de ambiente
   - `tldextract`: Extração confiável de TLD

## ⚙️ Como Usar

Para executar este projeto em sua máquina local, siga os passos abaixo.

**1. Clone o Repositório**

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

**2. Instale as Dependências**
É recomendado criar um ambiente virtual.

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

**3. Configure a Chave de API**

  - Crie um arquivo chamado `.env` na raiz do projeto.
  - Dentro dele, adicione sua chave de API do VirusTotal:
    ```
    API_KEY_VIRUSTOTAL="sua_chave_secreta_aqui"
    ```

**4. Execute o Programa**

### Análise de URL Única
```bash
python3 src/main.py --url "http://example.com"
python3 src/main.py -u "http://example.com"
```

### Análise de Múltiplas URLs
```bash
# Análise completa (com VirusTotal)
python3 src/main.py --file urls_test.txt

# Análise rápida (sem VirusTotal)
python3 src/main.py --file urls_test.txt --speed
python3 src/main.py -f urls_test.txt -s
```

### Formato do Arquivo de URLs
Crie um arquivo de texto (ex: `urls_test.txt`) com uma URL por linha:
```
http://example.com
https://suspicious-site.com
http://bit.ly/shortlink
```

### Argumentos Disponíveis

| Argumento | Forma Curta | Descrição | Obrigatório |
|-----------|-------------|-----------|-------------|
| `--url` | `-u` | Analisa uma única URL específica | Sim* |
| `--file` | `-f` | Analisa múltiplas URLs de um arquivo texto | Sim* |
| `--speed` | `-s` | Executa análise rápida (sem VirusTotal) | Não |
| `--help` | `-h` | Mostra a mensagem de ajuda com todos os argumentos | Não |

*\*Você deve usar apenas uma das opções: `--url` OU `--file`*

### Obter Ajuda

Para ver todos os argumentos disponíveis e exemplos de uso:

```bash
python3 src/main.py --help
python3 src/main.py -h
```

### Exemplos de Uso

```bash
# Analisar uma URL específica
python3 src/main.py --url "https://example.com"

# Analisar URLs de um arquivo
python3 src/main.py --file urls_list.txt

# Análise rápida sem consultar VirusTotal
python3 src/main.py --file urls_list.txt --speed

# Usando formas curtas dos argumentos
python3 src/main.py -u "https://example.com"
python3 src/main.py -f urls_list.txt -s
```

## 📄 Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.