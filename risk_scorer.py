def calculate_risk(pii_data):

    score = 0

    for item in pii_data:

        if item["type"] == "Email":
            score += 10

        elif item["type"] == "Phone":
            score += 20

        elif item["type"] in ["GitHub", "LinkedIn"]:
            score += 5

        elif item["type"] == "ID/Passport":
            score += 40

    if score >= 60:
        level = "CRITICAL"
    elif score >= 40:
        level = "HIGH"
    elif score >= 20:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level
    }

def calculate_privacy_score(risk_score):

    privacy_score = max(0, 100 - risk_score)

    if privacy_score >= 80:
        grade = "A"

    elif privacy_score >= 60:
        grade = "B"

    elif privacy_score >= 40:
        grade = "C"

    else:
        grade = "D"

    return {
        "privacy_score": privacy_score,
        "grade": grade
    }