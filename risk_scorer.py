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