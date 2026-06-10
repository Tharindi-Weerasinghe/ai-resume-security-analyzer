from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(filename, pii, risk, entities, urls):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Resume Security Report", styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"Risk Level: {risk['level']}", styles["Normal"]))
    content.append(Paragraph(f"Score: {risk['score']}", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("PII Findings:", styles["Heading2"]))
    for item in pii:
        content.append(Paragraph(f"{item['type']} - {item['matches']} - {item['risk']}", styles["Normal"]))

    content.append(Spacer(1, 12))

    content.append(Paragraph("Entities:", styles["Heading2"]))
    content.append(Paragraph(str(entities), styles["Normal"]))

    content.append(Spacer(1, 12))

    content.append(Paragraph("URL Analysis:", styles["Heading2"]))
    content.append(Paragraph(str(urls), styles["Normal"]))

    doc.build(content)