import re

def detect_pii(text):
    contact_info = []
    privacy_risks = []

    patterns = {
        "Email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        "Phone Number": r'\b(?:\+94|0)?7\d{8}\b',
        "LinkedIn URL": r'(?:https?://)?(?:www\.)?linkedin\.com/in/[a-zA-Z0-9\-_/]+',
        "GitHub URL": r'(?:https?://)?(?:www\.)?github\.com/[a-zA-Z0-9\-_/]+',

        "ID/Passport": r'\b[A-Z]{1,2}\d{6,9}\b',
        "Date of Birth": r'\b(?:DOB|Date of Birth|Born)[:\s]*\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',
        "Credit Card Number": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
        "Bank Account Number": r'\b(?:Account No|Account Number|Bank Account)[:\s]*\d{8,16}\b'
    }

    for label, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)

        if matches:
            if label in ["Email", "Phone Number", "LinkedIn URL", "GitHub URL"]:
                contact_info.append({
                    "type": label,
                    "matches": matches,
                    "status": "NORMAL"
                })
            else:
                privacy_risks.append({
                    "type": label,
                    "matches": matches,
                    "risk": risk_level(label)
                })

    return contact_info, privacy_risks


def risk_level(label):
    if label in ["ID/Passport", "Credit Card Number", "Bank Account Number"]:
        return "HIGH"
    elif label == "Date of Birth":
        return "MEDIUM"
    else:
        return "LOW"