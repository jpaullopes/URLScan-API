from flask import Flask, request, jsonify
from src.core.phishing_analyzer import PhishingAnalyzer
from src.core.ml_analyzer import analyze_with_ml

app = Flask(__name__)

# Instancia o analisador (ele vai carregar o config.json)
phishing_analyzer = PhishingAnalyzer()

@app.route("/analyze", methods=["POST"])
def analyze_url():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "URL não fornecida"}), 400

    url = data["url"]
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    print(f"Analisando URL: {url}")

    # 1. Análise Híbrida (Heurística + Features para ML)
    hybrid_analysis_results = phishing_analyzer.analyze(url)

    # 2. Análise com Machine Learning
    ml_features = hybrid_analysis_results["ml_features"]
    ml_analysis_result = analyze_with_ml(ml_features)

    # 3. Montagem da Resposta Final
    final_response = {
        "url": url,
        "analise_ml": ml_analysis_result,
        "analise_heuristica": hybrid_analysis_results["heuristic_results"]
    }

    return jsonify(final_response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
