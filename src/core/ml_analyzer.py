
import joblib
import pandas as pd

# Carrega o modelo treinado uma vez quando o módulo é importado
try:
    modelo = joblib.load("modelo_phishing.joblib")
except FileNotFoundError:
    print("ERRO: Arquivo 'modelo_phishing.joblib' não encontrado. Execute o script de treinamento.")
    modelo = None

# A ordem das features DEVE ser a mesma usada no treinamento
FEATURE_ORDER = [
    'nb_www',
    'ratio_digits_url',
    'domain_in_title',
    'domain_age',
    'phish_hints',
    'nb_hyperlinks',
    'ip',
    'nb_qm'
]

def analyze_with_ml(features_ml: dict) -> dict:
    """
    Usa o modelo de ML para prever se uma URL é phishing e retorna a confiança.
    """
    if not modelo:
        return {
            "previsao": "erro_modelo_nao_carregado",
            "confianca": "0%"
        }

    try:
        # Cria um DataFrame na ordem correta que o modelo espera
        input_df = pd.DataFrame([features_ml], columns=FEATURE_ORDER)
        
        # Faz a previsão de probabilidade
        # O resultado é uma lista de listas, ex: [[prob_legit, prob_phish]]
        probabilities = modelo.predict_proba(input_df)
        prediction = modelo.predict(input_df)

        # Pega a probabilidade da classe prevista
        confidence = probabilities[0][1] if prediction[0] == 'phishing' else probabilities[0][0]
        
        return {
            "previsao": prediction[0],
            "confianca": f"{confidence:.0%}"
        }
    except Exception as e:
        print(f"Erro durante a predição do modelo: {e}")
        return {
            "previsao": "erro_na_predicao",
            "confianca": "0%"
        }
