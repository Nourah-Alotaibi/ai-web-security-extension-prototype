from flask import Flask, request, jsonify
from gpt_utils import run_gpt_analysis
from securityheaders_utils import check_security_headers
from zap_utils import run_zap_scan
from shodan_utils import get_shodan_info
from risk_score import calculate_risk_score
from urllib.parse import urlparse

app = Flask(__name__)

def extract_domain(url):
    return urlparse(url).netloc

@app.route("/analyze", methods=["POST"])
def analyze_all():
    data = request.json
    html = data.get("html")
    url = data.get("url")
    domain = extract_domain(url)

    ai_report = run_gpt_analysis(html)
    headers_report = check_security_headers(url)
    zap_alerts = run_zap_scan(url)
    shodan_data = get_shodan_info(domain)
    risk_scores = calculate_risk_score(zap_alerts)

    return jsonify({
        "ai_insights": ai_report,
        "headers": headers_report,
        "zap_alerts": zap_alerts,
        "shodan": shodan_data,
        "risk_ranking": risk_scores
    })

if __name__ == "__main__":
    app.run(debug=True)
