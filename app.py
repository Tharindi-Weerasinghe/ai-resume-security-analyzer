from flask import Flask, render_template, request
import os
from ai_entity_detector import extract_entities
from url_security import analyze_urls
from pdf_report import generate_pdf

from extractor import extract_text
from pii_detector import detect_pii
from risk_scorer import calculate_risk

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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

    
    return render_template(
        "report.html",
        pii=pii_results,
        risk=risk_result,
        preview=text[:800],
        entities=entities,
        urls=urls,
        pdf_file = "report.pdf"
    )

if __name__ == "__main__":
    app.run(debug=True)