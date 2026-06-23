def calculate_risk(privacy_risks, urls):
    score = 0

    for item in privacy_risks:
        if item["risk"] == "HIGH":
            score += 40
        elif item["risk"] == "MEDIUM":
            score += 20
        else:
            score += 10

    for url in urls:
        if url["risk"] == "HIGH":
            score += 30
        elif url["risk"] == "MEDIUM":
            score += 15

    if score >= 70:
        level = "CRITICAL"
    elif score >= 45:
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