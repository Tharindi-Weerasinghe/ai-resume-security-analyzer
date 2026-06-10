def generate_recommendations(pii_findings):

    recommendations = []

    for item in pii_findings:

        pii_type = item["type"]

        if pii_type == "Passport Number":
            recommendations.append(
                "Remove passport information before sharing resumes publicly."
            )

        elif pii_type == "Phone Number":
            recommendations.append(
                "Consider using a dedicated professional contact number."
            )

        elif pii_type == "Email":
            recommendations.append(
                "Use a professional email address and avoid exposing personal emails unnecessarily."
            )

        elif pii_type == "Home Address":
            recommendations.append(
                "Avoid including your full home address unless specifically required."
            )

        elif pii_type == "LinkedIn URL":
            recommendations.append(
                "Ensure your LinkedIn profile visibility settings are configured appropriately."
            )

    return recommendations