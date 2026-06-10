import pdfplumber
from docx import Document

def extract_text(filepath):

    if filepath.endswith('.pdf'):
        with pdfplumber.open(filepath) as pdf:
            text = ''

            for page in pdf.pages:
                text += page.extract_text() or ""
            return text

    elif filepath.endswith(".docx"):
        doc = Document(filepath)

        return "\n" .join(
            para.text for para in doc.paragraphs
        )
    
        return ""


       