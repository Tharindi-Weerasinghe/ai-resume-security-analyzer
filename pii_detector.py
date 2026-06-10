import re

def detect_pii(text):
    findings = []

    patterns = {
        "Email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        "Phone": r'(\+?\d[\d\s\-]{7,15}\d)',
        "LinkedIn": r'linkedin\.com/in/[a-zA-Z0-9\-]+',
        "GitHub": r'github\.com/[a-zA-Z0-9\-]+',
        "ID/Passport": r'\b[A-Z0-9]{6,12}\b'
    }

    for label, pattern in patterns.items():
        matches = re.findall(pattern, text)

        if matches:
            findings.append({
                "type": label,
                "matches": matches,
                "risk": risk_level(label)
            })

    return findings


def risk_level(label):
    if label == "ID/Passport":
        return "HIGH"
    elif label == "Phone":
        return "MEDIUM"
    else:
        return "LOW"