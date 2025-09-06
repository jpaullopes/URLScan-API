import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib


dataframe = pd.read_parquet("src/data/Testing.parquet")

#print(dataframe.info())

# Verifica se as colunas existem no dataset
print("Colunas disponíveis no dataset:")
print(dataframe.columns.tolist())
print("\nFormato dos dados:")
print(dataframe.info())

features_escolhidas = [
    'nb_www',
    'ratio_digits_url',
    'domain_in_title',
    'domain_age',
    'phish_hints',
    'nb_hyperlinks',
    'ip',
    'nb_qm'
]

# Verifica se todas as features existem no dataset
features_existentes = [col for col in features_escolhidas if col in dataframe.columns]
features_faltantes = [col for col in features_escolhidas if col not in dataframe.columns]


if not features_existentes:
    print("ERRO: Nenhuma das features especificadas foi encontrada no dataset!")
    exit(1)

# Usa apenas as features que existem
dados_selecionados = dataframe[features_existentes + ['status']]

# Remove linhas com valores ausentes
dados_selecionados = dados_selecionados.dropna()

# X recebe as features
X = dados_selecionados[features_existentes]

# y recebe APENAS a coluna 'status'
y = dados_selecionados['status']



# Dividindo os dados: 80% para treino, 20% para teste
# O 'stratify=y' garante que a proporção de phishing/legítimo seja a mesma nos dois conjuntos
try:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Dados de treino: {X_train.shape}")
    print(f"Dados de teste: {X_test.shape}")
except ValueError as e:
    print(f"Erro na divisão dos dados: {e}")
    print("Tentando sem stratify...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

print("\nTreinando o modelo...")
modelo = LogisticRegression(max_iter=1000)

try:
    modelo.fit(X_train, y_train)
    print("Modelo treinado com sucesso!")
except Exception as e:
    print(f"Erro ao treinar o modelo: {e}")
    exit(1)

# Pedimos ao modelo para classificar os dados de teste
previsoes = modelo.predict(X_test)

# Calculamos a acurácia (porcentagem de acertos)
acuracia = accuracy_score(y_test, previsoes)

print(f"\nResultados do modelo:")
print(f"Acurácia: {acuracia:.4f} ({acuracia*100:.2f}%)")
print(f"\nRelatório detalhado:")
print(classification_report(y_test, previsoes))

# Salva o modelo treinado
nome_do_arquivo = 'modelo_phishing.joblib'
joblib.dump(modelo, nome_do_arquivo)
print(f"\nModelo salvo como: {nome_do_arquivo}")

# Teste de carregamento do modelo
modelo_carregado = joblib.load(nome_do_arquivo)
print("Modelo carregado com sucesso!")