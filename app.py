from flask import Flask, render_template, request
import os
from ai_entity_detector import extract_entities
from url_security import analyze_urls
from pdf_report import generate_pdf
from recommendations import generate_recommendations
from extractor import extract_text
from pii_detector import detect_pii
from risk_scorer import calculate_risk
from risk_scorer import calculate_privacy_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def generate_summary(risk):
    if risk["level"] == "CRITICAL":
        return "Critical risk: Sensitive data exposure + potential security threats detected."
    elif risk["level"] == "HIGH":
        return "High risk: Resume contains sensitive personal information."
    elif risk["level"] == "MEDIUM":
        return "Medium risk: Some personal data exposure detected."
    else:
        return "Low risk: Resume is relatively safe."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["resume"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    text = extract_text(filepath)

    pii_results = detect_pii(text)
    risk_result = calculate_risk(pii_results)
    entities = extract_entities(text)

    urls = analyze_urls(text)
    pdf_path = os.path.join(UPLOAD_FOLDER, "report.pdf")

    generate_pdf(pdf_path, pii_results, risk_result, entities, urls)

    summary = generate_summary(risk_result)
    recommendations = generate_recommendations(pii_results)
    privacy = calculate_privacy_score(risk_result["score"])

    
    return render_template(
        "report.html",
        pii=pii_results,
        risk=risk_result,
        preview=text[:800],
        entities=entities,
        urls=urls,
        pdf_file = "report.pdf",
        summary=summary,
        recommendations=recommendations,
        privacy=privacy
    )


if __name__ == "__main__":
    app.run(debug=True)