# 🕵️ Phishing Analyzer Tool
![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Status](https://img.shields.io/badge/status-active-brightgreen)

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
    CHAVE_API_VIRUSTOTAL="sua_chave_secreta_aqui"
    ```

**4. Execute o Programa**

```bash
python3 main.py
```

O programa irá solicitar que você insira a URL para análise.

