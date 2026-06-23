from flask import Flask, render_template, request, send_from_directory
import os

from ai_entity_detector import extract_entities
from url_security import analyze_urls
from pdf_report import generate_pdf
from recommendations import generate_recommendations
from extractor import extract_text
from pii_detector import detect_pii
from risk_scorer import calculate_risk, calculate_privacy_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def generate_summary(risk):
    if risk["level"] == "CRITICAL":
        return "Critical risk: The resume contains unnecessary sensitive information or risky links that should be reviewed before sharing publicly."
    elif risk["level"] == "HIGH":
        return "High risk: The resume contains sensitive information that is not usually required for initial job applications."
    elif risk["level"] == "MEDIUM":
        return "Medium risk: Some privacy exposure was detected. Review the highlighted items before sharing."
    else:
        return "Low risk: Only normal resume contact information or minimal privacy exposure was detected."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["resume"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    text = extract_text(filepath)

    contact_info, privacy_risks = detect_pii(text)
    urls = analyze_urls(text)
    entities = extract_entities(text)

    risk_result = calculate_risk(privacy_risks, urls)
    privacy = calculate_privacy_score(risk_result["score"])
    summary = generate_summary(risk_result)
    recommendations = generate_recommendations(privacy_risks, urls)

    pdf_path = os.path.join(UPLOAD_FOLDER, "report.pdf")
    generate_pdf(pdf_path, privacy_risks, risk_result, entities, urls)

    return render_template(
        "report.html",
        contact_info=contact_info,
        privacy_risks=privacy_risks,
        risk=risk_result,
        privacy=privacy,
        entities=entities,
        urls=urls,
        summary=summary,
        recommendations=recommendations
    )


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)