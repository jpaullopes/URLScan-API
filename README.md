# Phishing Analyzer Tool

Analisador de URLs para detecção de características de phishing, desenvolvido como um projeto de portfólio para demonstrar habilidades em análise de segurança e desenvolvimento em Python.

## Descrição

Este projeto é uma ferramenta de linha de comando que avalia uma URL e calcula uma pontuação de risco com base em uma série de verificações heurísticas. O objetivo é automatizar a análise inicial de links suspeitos, fornecendo um veredito rápido sobre o potencial de risco.

A lógica de análise é encapsulada na classe `PhishingAnalyzer` e as configurações (pesos, TLDs, etc.) são gerenciadas externamente através do arquivo `src/config.json`.

## Funcionalidades

O analisador utiliza uma abordagem multifacetada para avaliar as URLs, verificando os seguintes pontos:

### Análise Heurística (Interna)

- **Uso de Endereço IP:** Detecta se a URL usa um endereço IP em vez de um nome de domínio.
- **Caractere de Ofuscação (`@`):** Verifica a presença do caractere `@` na URL.
- **Excesso de Subdomínios:** Alerta para URLs com um número excessivo de subdomínios.
- **TLD Suspeito:** Compara o Top-Level Domain com uma lista de TLDs configurada no `src/config.json`.
- **Link Encurtado:** Identifica se a URL pertence a um serviço de encurtamento de links.
- **Comprimento Excessivo:** Sinaliza URLs anormalmente longas.

### Inteligência Externa

- **Integração com VirusTotal:** Utiliza a API do VirusTotal para checar a reputação da URL.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Bibliotecas Principais:**
  - `tldextract`
  - `python-dotenv`

## Como Usar

**1. Clone o Repositório**

```bash
git clone <URL_DO_REPOSITORIO>
cd phishing_link_analysis
```

**2. Instale as Dependências**

É recomendado criar um ambiente virtual.
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale o projeto em modo editável:
```bash
pip install -e .
```
Para instalar as dependências de desenvolvimento, use:
```bash
pip install -e ".[dev]"
```

**3. Configure a Chave de API**

Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave de API do VirusTotal:
```
API_KEY_VIRUSTOTAL="sua_chave_secreta_aqui"
```

**4. Execute o Programa**

### Análise de URL Única
```bash
Phishing-link-analysis --url "http://example.com"
```

### Análise de Múltiplas URLs
```bash
# Análise completa (com VirusTotal)
Phishing-link-analysis --file urls.txt

# Análise rápida (sem VirusTotal)
Phishing-link-analysis --file urls.txt --speed
```

### Argumentos Disponíveis

| Argumento | Forma Curta | Descrição | Obrigatório |
|-----------|-------------|-----------|-------------|
| `--url` | `-u` | Analisa uma única URL específica | Sim* |
| `--file` | `-f` | Analisa múltiplas URLs de um arquivo texto | Sim* |
| `--speed` | `-s` | Executa análise rápida (sem VirusTotal) | Não |
| `--help` | `-h` | Mostra a mensagem de ajuda com todos os argumentos | Não |

*\*Você deve usar apenas uma das opções: `--url` OU `--file`*

**5. Configuração da Análise**

Os parâmetros da análise heurística (pesos de pontuação, listas de TLDs, etc.) podem ser modificados diretamente no arquivo `src/config.json`.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
