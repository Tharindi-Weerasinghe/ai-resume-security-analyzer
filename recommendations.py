def generate_recommendations(privacy_risks, urls):
    recommendations = []

    for item in privacy_risks:
        if item["type"] == "ID/Passport":
            recommendations.append("Remove passport or national ID details before sharing your resume publicly.")
        elif item["type"] == "Date of Birth":
            recommendations.append("Avoid including your full date of birth unless the employer specifically requires it.")
        elif item["type"] == "Credit Card Number":
            recommendations.append("Never include credit card numbers in a resume.")
        elif item["type"] == "Bank Account Number":
            recommendations.append("Never include bank account details in a resume.")

    for url in urls:
        if url["risk"] in ["HIGH", "MEDIUM"]:
            recommendations.append("Review suspicious or shortened URLs before sharing your resume.")

    if not recommendations:
        recommendations.append("No unnecessary high-risk personal information was detected.")

    return recommendations