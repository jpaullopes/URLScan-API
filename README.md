# Phishing Analyzer API

Uma API web desenvolvida com Flask para análise híbrida de URLs, combinando Machine Learning e regras heurísticas para detecção de phishing. Este projeto serve como um portfólio para demonstrar habilidades em desenvolvimento web, segurança da informação e Machine Learning.

## Descrição

Esta ferramenta oferece um endpoint HTTP POST que recebe uma URL e retorna uma análise detalhada, incluindo:

-   **Análise de Machine Learning:** Previsão (`phishing` ou `legitimate`) e um score de confiança.
-   **Análise Heurística:** Uma pontuação de risco, nível de risco (`Baixo`, `Médio`, `Alto`, `Crítico`) e uma lista de regras heurísticas acionadas.

A lógica de análise é modularizada em classes Python, e as configurações heurísticas são gerenciadas externamente via `config.json`.

## Funcionalidades

### Análise de Machine Learning

Utiliza um modelo de Regressão Logística treinado para classificar URLs como phishing ou legítimas, fornecendo uma probabilidade de confiança para a previsão.

### Análise Heurística

Avalia a URL com base em um conjunto de regras e características, atribuindo pontos de risco. As regras incluem:

-   **Uso de Endereço IP:** Detecta se o domínio é um IP numérico.
-   **Presença de 'www':** Verifica a ocorrência de 'www' no subdomínio.
-   **Proporção de Dígitos na URL:** Calcula a densidade de dígitos na URL.
-   **Número de '?' na URL:** Conta a ocorrência de pontos de interrogação.
-   **Palavras Suspeitas (Phish Hints):** Identifica termos comuns em ataques de phishing (ex: 'login', 'verify', 'account').
-   **Idade do Domínio:** Verifica a idade do domínio (domínios muito novos são suspeitos).
-   **Número de Hiperlinks:** Conta a quantidade de links na página (pode indicar conteúdo malicioso).
-   **Domínio no Título:** Verifica se o domínio principal está presente no título da página.
-   **URL Longa:** Sinaliza URLs com comprimento excessivo.
-   **TLD Suspeito:** Compara o Top-Level Domain com uma lista de TLDs conhecidos por serem usados em phishing.
-   **Excesso de Subdomínios:** Alerta para URLs com muitos subdomínios.
-   **Link Encurtado:** Identifica se a URL usa um serviço de encurtamento.
-   **Ofuscação com '@':** Verifica a presença do caractere '@' na URL.
-   **Página Não Acessível:** Atribui pontos se a URL não puder ser acessada.

## Tecnologias Utilizadas

-   **Linguagem:** Python 3.12+
-   **Framework Web:** Flask
-   **Bibliotecas Principais:**
    -   `tldextract`: Extração de componentes de URL.
    -   `requests`: Requisições HTTP.
    -   `BeautifulSoup4`: Parsing HTML.
    -   `python-whois`: Consulta de informações WHOIS de domínios.
    -   `scikit-learn`: Treinamento e uso do modelo de Machine Learning.
    -   `pandas`: Manipulação de dados.
    -   `joblib`: Serialização de modelos ML.

## Como Usar

### 1. Clone o Repositório

```bash
git clone https://github.com/jpaulo/phishing_link_analysis.git # Substitua pela URL real do seu repositório
cd phishing_link_analysis
```

### 2. Instale as Dependências

É altamente recomendado usar um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate # No Windows, use `.venv\Scripts\activate`
pip install -r requirements.txt # Ou `uv pip install -r requirements.txt` se estiver usando uv
```

**Nota:** As dependências são gerenciadas via `pyproject.toml` e `uv.lock`. Você pode gerar o `requirements.txt` a partir do `uv.lock` se preferir, ou instalar diretamente com `uv pip install -e .`

### 3. Obtenha o Dataset

O modelo de Machine Learning é treinado com base em um dataset. Você pode baixá-lo do Kaggle:

[Phishing URL Dataset on Kaggle](https://www.kaggle.com/datasets/hemanthpingali/phishing-url?resource=download&select=Training.parquet)

Após baixar o arquivo `Training.parquet`, renomeie-o para `Testing.parquet` e coloque-o no diretório `src/data/`.

### 4. Treine o Modelo

Execute o script de treinamento para gerar o arquivo `modelo_phishing.joblib`:

```bash
python src/core/train_model.py
```

### 5. Configure a Análise Heurística

Os pesos das regras, TLDs suspeitos e encurtadores de URL são configurados no arquivo `config.json` na raiz do projeto. Você pode ajustá-lo conforme suas necessidades.

### 6. Execute o Servidor Flask

```bash
flask --app app run --host 0.0.0.0 --port 5000
```

O servidor estará rodando em `http://0.0.0.0:5000`.

### 7. Teste a API

Abra um novo terminal e envie requisições POST para o endpoint `/analyze`:

**Exemplo de URL Legítima:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://www.google.com"}' http://127.0.0.1:5000/analyze
```

**Exemplo de URL Suspeita:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "http://secure-login-bancodobrasil.com-update.info/personal-data"}' http://127.0.0.1:5000/analyze
```

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.