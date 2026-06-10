# AI Resume Security Analyzer 🔐

## Overview
This project is an AI-powered cybersecurity tool that analyzes resumes for sensitive data exposure, phishing risks, and personal information leaks.

It helps users understand security risks in their resumes before submitting them to job portals.

---

## 🚀 Features

- 📄 Resume upload (PDF support)
- 🔍 PII detection (email, phone, ID leaks)
- 🧠 AI entity recognition (spaCy NLP)
- 🌐 URL phishing detection
- 📊 Risk scoring system (LOW → CRITICAL)
- 📄 Automatic PDF report generation
- 🧾 Web-based security dashboard

---

## 🛠️ Tech Stack

- Python
- Flask
- spaCy (NLP)
- pdfplumber
- ReportLab
- Regex (security patterns)

---

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python app.py